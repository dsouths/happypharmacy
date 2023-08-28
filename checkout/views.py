from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse

from .forms import OrderForm, CouponApplyForm
from .models import Order, OrderLineItem, Coupon
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    coupon_id = request.session.get('coupon_id')
    discount = 0

    if coupon_id:
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            if coupon.active:
                discount = coupon.discount
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    # Apply the discount to the total price
    total = float(current_bag['grand_total'])
    total = total - discount
    request.session['total'] = total
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            print("Order after Save:", order.__dict__)
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your bag wasn't found in our database. Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('view_bag'))
            order.update_total
            order.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout:checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
            print("Order Form Errors:", order_form.errors)
    else:
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        order_form = OrderForm()

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'discount': discount,
        'grand_total': total,  # Include the updated total
    }

    return render(request, template, context)


def apply_coupon(request):
    total = float(request.session.get('total', 0))  # Retrieve the total from the session and convert to float
    code = request.POST.get('code')
    try:
        coupon = Coupon.objects.get(code=code)
        if coupon.active:
            if coupon.discount_type == 'fixed':
                discount = float(coupon.discount_value)
            else:  # Assume percentage
                discount = float(total * (float(coupon.discount_value) / 100))  # Convert discount_value to float

            # Check if a discount has already been applied and is above €0.00
            existing_discount = float(request.session.get('discount', 0))
            if existing_discount > 0:
                return JsonResponse({'success': False, 'error': 'A discount has already been applied'})
            elif existing_discount == 0:
                # Allow the user to apply a new coupon if the existing discount is zero
                pass

            new_total = total - discount
            request.session['total'] = new_total  # Update the total in the session here
            request.session['discount'] = discount
            return JsonResponse({'success': True, 'new_total': new_total, 'discount': discount})
        else:
            return JsonResponse({'success': False, 'error': 'Coupon is not active'})
    except Coupon.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid coupon code'})


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    print("Order in checkout_success:", order.__dict__)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order_items = order.lineitems.all()
        order.save()
        for order_item in order_items:
            if order_item.product.stock_level - order_item.quantity >= 0:

                order_item.product.stock_level = order_item.product.stock_level - order_item.quantity
                order_item.product.save()
            else:
                messages.error(
                    request,
                    f'Not enough stock available. Please contact us for more information.')


        request.session['discount'] = 0


        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

            print("Session Data:", request.session)
            print("Order Object:", order.__dict__)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
