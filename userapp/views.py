from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout ,update_session_auth_hash

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm ,SetPasswordForm

@login_required(login_url='user_login')
def home(request):
    return render(request , 'home.html')

def signup(request):
    context = {}  

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        context['username'] = username
        context['email'] = email

        if password != confirm_password:
            context['password_error'] = "Passwords do not match"

        elif User.objects.filter(username=username).exists():
            context['username_error'] = "Username already exists"

        elif User.objects.filter(email=email).exists():
            context['email_error'] = "Email already registered"

        else:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('user_login')

    return render(request, 'signup.html', context)



def user_login(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password")
            
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')




def password_change(request):
    if request.user.is_authenticated:  # ✅ Correct: is_authenticated (not is_authenticate)
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)  # ✅ Correct: user=request.user
            if fm.is_valid():
                user = fm.save()
                update_session_auth_hash(request, user)  # ✅ Keep user logged in after password change
                return redirect('home')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {'form': fm})
    else:
        return redirect('user_login')
    
    
def password_change1(request):
    if request.user.is_authenticated:  # ✅ Correct: is_authenticated (not is_authenticate)
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)  # ✅ Correct: user=request.user
            if fm.is_valid():
                user = fm.save()
                update_session_auth_hash(request, user)  # ✅ Keep user logged in after password change
                return redirect('home')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'forgot.html', {'form': fm})
    else:
        return redirect('user_login')
