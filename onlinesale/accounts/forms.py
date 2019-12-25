from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User

#DjangoFormFields
class SignInForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}))
    pwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    

class RegisterForm(forms.Form):
    firstname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    lastname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    pwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    cpwd = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    
    def clean(self):
        if self.cleaned_data.get('pwd') != self.cleaned_data.get('cpwd'):
            raise ValidationError("Both passwords don't match")
        return self.cleaned_data

    def clean_username(self):
        if User.objects.filter(username__exact=self.cleaned_data.get('username')).exists():
            raise ValidationError("Username already in use.")
        return self.cleaned_data.get('username')