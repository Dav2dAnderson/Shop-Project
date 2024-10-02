from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseForbidden

from .models import User

# Create your views here.


class RegistrationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseForbidden("Siz allaqachon tizimga kirgansiz!\nBoshqatdan registratsiya qilishi uchun tizimdan chiqing.")
        return render(request, "registration/registration.html")
    
    def post(self, request):
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("confirmation_password")

        if password != password_confirmation:
            messages.warning(request, "Password-ni qaytadan tering!")
            return redirect(reverse("registration"))
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Bunday user allaqachon mavjud!")
            return redirect(reverse("registration"))
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Bu email-da bo'lgan user mavjud!")
            return redirect(reverse("registration"))
        if User.objects.filter(phone_number=phone_number).exists():
            messages.warning(request, "Bu telefon raqamda bo'lgan user mavjud!")
            return redirect(reverse("registration"))
        
        try:
            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                address=address,
                phone_number=phone_number,
                password=password
            )
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect(reverse("home"))
        
        except:
            messages.error(request, "Error")
            return redirect(reverse("registration"))
    

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseForbidden("Siz allaqachon tizimga kirgansiz!\nBoshqatdan kirish uchun tizimdan chiqing!")
        return render(request, "registration/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Bunday user mavjud emas!")
            return redirect(reverse("login"))
        user = User.objects.get(username=username)
        
        if not user.check_password(password):
            messages.warning(request, 'Password is incorrect')
            return redirect(reverse('login'))
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli tizimga kirdingiz!")
            return redirect(reverse("home"))
        else:
            messages.error(request, "Error")
        return redirect(reverse("login"))


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("home"))
