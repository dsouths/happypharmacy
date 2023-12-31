from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    """renders the contact form"""
    class Meta:
        fields = ['name', 'email', 'phone_number', 'subject', 'message', 'contact_type', 'rating']
        model = Message
        widgets = {
            'rating': forms.RadioSelect, # Render rating as radio buttons
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'subject': 'Subject',
            'message': 'Your message',
            'contact_type': 'Contact Type',
            'rating': 'Rating (Only for testimonials)',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

