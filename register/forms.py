from django import forms
from .models import user, vehicle

class FormUser(forms.ModelForm):
    class Meta:
        model = user
        exclude = () 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autofocus': '', 'style': 'width: 300px'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '111.222.333-44', 'pattern' : '[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', 'autocomplete':'off', 'onkeyup': 'cpf_mask()', 'style': 'width: 300px'}),
            'enrollment': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off', 'style': 'width: 300px'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete':'off', 'style': 'width: 300px'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 22222-3333', 'onkeyup': 'phone_mask()', 'onfocus': 'phone_mask_focus()', 'onBlur': 'phone_mask_blur()', 'autocomplete':'off', 'style': 'width: 300px'})
        }

class FormVeh(forms.ModelForm):
    class Meta:
        model = vehicle
        exclude = () 
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'autofocus': '', 'style': 'width: 300px'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'plate': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px', 'autocomplete':'off'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'user': forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px'})
        }