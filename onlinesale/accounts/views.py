from django.shortcuts import render, redirect
from .forms import RegisterForm, SignInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signout_page(request):
    logout(request)
    return redirect("/")

def signin_page(request):
    signinform = SignInForm(request.POST or None)
    context = {
        'signinform':signinform,
    }
    if signinform.is_valid():
        user = authenticate(username=signinform.data.get('username'), password=signinform.data.get('pwd'))
        if user:
            login(request, user)
            # return redirect("/")
            return redirect("home")
        else:
            context['errMsg'] = "Invalid Credentials"
    return render(request, "accounts/login.html", context)

def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    #form = RegisterForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        un=form.cleaned_data.get('username')
        fn=form.cleaned_data.get('firstname')
        ln=form.cleaned_data.get('lastname')
        email=form.cleaned_data.get('email')
        pwd=form.cleaned_data.get('pwd')
        user = User.objects.create_user(username=un,password=pwd,email=email,first_name=fn,last_name=ln)
        if user:
            context['msg'] = "User Has been created successfully."
            context['form'] = RegisterForm()
        else:
            context['msg'] = "Something went wrong please try again"
    return render(request, "accounts/register.html", context)
