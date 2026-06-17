from .models import Contact
from django.forms import ModelForm
from django import forms


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = {'name', 'surname', 'email', 'phone'}

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Name'}
            ),
            'surname': forms.TextInput(
                attrs = {
                    'placeholder': 'Surname'}
            ),
            'email': forms.TextInput(
                attrs = {
                    'placeholder': 'Email'}
            ),
            'phone': forms.TextInput(
                attrs = {
                    'placeholder': 'Phone number'}
            )
        }