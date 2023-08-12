from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages


# Create your views here.

def message(request):
    """Saves contact form input to db"""
    form = MessageForm()
    if request.method == 'POST' and request.user.is_authenticated:

        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent to admin!')

            return render(request, "home/index.html")
        else:
            messages.error(
                request,
                'Failed to send message. Please ensure the form is valid.')
    else:
        form = MessageForm()
        context = {
            'form': form,
        }
        return render(request, 'contact/contact.html', context)

    return render(request, 'contact/contact.html')
