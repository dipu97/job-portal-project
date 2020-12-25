from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages,auth
# Create your views here.
from jobs.models import jobs
from Employee.models import Employee
from django.contrib.auth.models import User


def register(request):
    number = jobs.objects.all().count()
    print(request.POST)
    if request.method == 'POST':
        dict_method = request.POST.copy()
        first_name = dict_method.get('first_name')
        last_name = dict_method.get('last_name')
        username = dict_method.get('username')
        email = dict_method.get('email')
        password = dict_method.get('password')
        password2 = dict_method.get('password2')
        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'User already exit!')
                else:
                    User.objects.create_user(username=username,
                                             password=password,
                                             first_name=first_name,
                                             last_name=last_name,
                                             email=email
                    )
                    Employee.objects.create(name=first_name+last_name,
                                            email=email,
                                            phone=1,
                                            photo=True,
                                            message="Abc")

                    messages.success(request,'You are successfully registered!')
                    return HttpResponseRedirect(reverse('login'))

        else:
            messages.error(request, "Password doesn't Match ")

        return HttpResponseRedirect(reverse('register'))
    context = {
        'count': number,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        dict_method= request.POST.copy()
        username=dict_method.get('username')
        password=dict_method.get('password')
        print(password,username)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You have successfully logged in')
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid Username or Password')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'accounts/login.html')


def logout(request):

    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'Yor are successfully logged out')
        return HttpResponseRedirect(reverse('index'))


def dashboard(request):
    number=jobs.objects.all().count()
    jobss=jobs.objects.all()
    latest=jobs.objects.filter(is_published=True).order_by('-published_date')[:4]
    context={
        'count':number,
        'jobss':jobss,
        'latest':latest,
    }
    return render(request, 'accounts/dashboard.html',context)
