from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.Textarea(attrs={'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
                }
        fields = '__all__'
