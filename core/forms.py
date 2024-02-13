from django.forms import ModelForm
from .models import ContactUs
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'type': 'email', 'placeholder': 'Your Email'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Company Name'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Subject'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})



