from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .form import RegistrationForm,PasswordResetForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser,Log
from rest_framework import generics
from .serializers import UserSerializer, LogSerializer
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Count
from django.db.models.signals import post_save
from django.contrib import messages


def admin_required(view_func):
    return user_passes_test(lambda u: u.is_staff, login_url='/login/')(view_func)

def redirect_if_logged_in(user):
    return not user.is_authenticated



def home(request):
    user = request.user
    
    context ={
        'user':user,
    }

    return render(request, 'home.html', context)




@user_passes_test(redirect_if_logged_in, login_url='/')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Hash the password
            hashed_password = make_password(password)

            # Save user without password
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password='',  # Password will be set separately

            )

            # Set hashed password
            user.password = hashed_password
            user.save()

            messages.success(request, "Your account has been created successfully!")
            return redirect('/login')
        else:
            messages.error(request, "Some error occured check again!")


            

    else:
        form = RegistrationForm()
    

    return render(request, 'users/register.html', {'form': form})



@user_passes_test(redirect_if_logged_in, login_url='/')
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            messages.success(request, "Login successfully!")

            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')


@admin_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LogListView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class LogsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        logs = Log.objects.all().order_by('-timestamp')  # Latest logs first
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    Log.objects.create(user=user, action="User Login")

@receiver(user_logged_out) 
def log_user_logout(sender, request, user, **kwargs): 
    Log.objects.create(user=user, action="User Logout")

@receiver(post_save, sender=CustomUser)
def log_user_creation(sender, instance, created, **kwargs):
    if created: 
        Log.objects.create(user=instance, action="User Creation")

@receiver(post_save, sender=CustomUser)
def log_password_reset(sender, instance, update_fields, **kwargs):
    if update_fields and 'password' in update_fields:
        Log.objects.create(user=instance, action="Password Reset")



class UserActivityReportView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        report = Log.objects.values('user__username').annotate(actions=Count('id')).order_by('-actions')
        return Response(report)




def user_report(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    activities = Log.objects.filter(user=user)
    return render(request, 'users/user_report.html', {'user': user, 'activities': activities})


@user_passes_test(redirect_if_logged_in, login_url='/')
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Password  successfully reset!")

            return redirect('login')  # Redirect to the login page after resetting the password
    else:
        form = PasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})



