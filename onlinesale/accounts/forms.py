from django import forms
from django.forms import ValidationError
# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()

#DjangoFormFields
class SignInForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    pwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
class RegisterForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    fullname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}))
    mobile = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile'}))
    pwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    cpwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    
    def clean(self):
        if self.cleaned_data.get('pwd') != self.cleaned_data.get('cpwd'):
            raise ValidationError("Both passwords don't match")
        return self.cleaned_data

    def clean_email(self):
        if User.objects.filter(email__exact=self.cleaned_data.get('email')).exists():
            raise ValidationError("Email already in use.")
        return self.cleaned_data.get('email')