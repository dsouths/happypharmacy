from .forms import MessageForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Testimonial
from django.contrib.auth.decorators import login_required

@login_required
def contact_view(request):
    form = MessageForm()
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            if message.contact_type == 'testimonial':
                # Create a testimonial from the submitted message
                Testimonial.objects.create(
                    subject=message.subject,
                    content=message.message,
                    rating=message.rating,
                    name=message.name
                )
                messages.success(request, 'Testimonial submitted to admin!')
            else:
                messages.success(request, 'Message sent to admin!')

            return redirect('contact') 

        else:
            messages.error(
                request,
                'Failed to send message. Please ensure the form is valid.')

    context = {
        'form': form,
        'testimonials': testimonials,
    }

    return render(request, 'contact.html', context)
