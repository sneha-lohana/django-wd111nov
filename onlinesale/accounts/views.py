from django.shortcuts import render, redirect
from .forms import RegisterForm, SignInForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django.contrib.auth import get_user_model

User = get_user_model()
def signout_page(request):
    logout(request)
    return redirect("/")

def signin_page(request):
    signinform = SignInForm(request.POST or None)
    redirect_path = request.POST.get('next_url') or None
    # print(redirect_path)
    context = {
        'signinform':signinform,
    }
    if signinform.is_valid():
        user = authenticate(username=signinform.data.get('email'), password=signinform.data.get('pwd'))
        if user:
            login(request, user)
            if redirect_path is not None:
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
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
        email=form.data.get('email')
        fn=form.data.get('fullname')
        mobile=form.data.get('mobile')
        pwd=form.data.get('pwd')
        user = User.objects.create_user(email=email,password=pwd,full_name=fn,mobile=mobile)
        if user:
            context['msg'] = "User Has been created successfully."
            context['form'] = RegisterForm()
        else:
            context['msg'] = "Something went wrong please try again"
    return render(request, "accounts/register.html", context)
