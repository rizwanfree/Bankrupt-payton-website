from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'type': 'email', 'placeholder': 'Your Email'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Company Name'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'placeholder': 'Subject'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})

    class Meta(object):
        model = Contact
        fields = ['name', 'email', 'company_name', 'subject', 'content']
