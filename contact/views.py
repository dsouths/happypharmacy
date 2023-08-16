from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def message(request):
    """Saves contact form input to db"""
    form = MessageForm()
    if request.method == 'POST':

        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent to admin!')
            return redirect('contact')

        else:
            messages.error(
                request,
                'Failed to send message. Please ensure the form is valid.')
            return redirect('contact')
    else:
        form = MessageForm()
        context = {
            'form': form,
        }
        return render(request, 'contact.html', context)

    
