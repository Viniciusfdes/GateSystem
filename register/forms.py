from django import forms
from .models import user, vehicle

class FormUser(forms.ModelForm):
    class Meta:
        model = user
        exclude = () 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autofocus': '', 'style': 'width: 400px'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '111.222.333-44', 'pattern' : '[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', 'autocomplete':'off', 'onkeyup': 'cpf_mask()', 'style': 'width: 400px'}),
            'enrollment': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off', 'style': 'width: 400px'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete':'off', 'style': 'width: 400px'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 22222-3333', 'onkeyup': 'phone_mask()', 'onfocus': 'phone_mask_focus()', 'onBlur': 'phone_mask_blur()', 'autocomplete':'off', 'style': 'width: 400px'})
        }

class FormVeh(forms.ModelForm):
    class Meta:
        model = vehicle
        exclude = () 
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'autofocus': '', 'style': 'width: 400px'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px'}),
            'plate': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px', 'autocomplete':'off'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px'}),
            'user': forms.Select(attrs={'class': 'form-select', 'style': 'width: 400px'})
        }