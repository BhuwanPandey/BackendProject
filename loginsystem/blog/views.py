from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login as lg,authenticate

def login(request):
    if request.method=='POST':
        username,password=(request.body.decode('utf-8')).split('&')
        user=authenticate(username=username,password=password)
        if user is not None:
            lg(request,user)
            msg='success'
        else:
            msg='username and password doesnot match!'
        return JsonResponse({'msg':msg})
    return render(request,'blog/main.html')

def register(request):
    if request.method=='POST':
        username,password=(request.body.decode('utf-8')).split('&')
        try:
            user=User.objects.get(username=username)
            msg='error'
        except User.DoesNotExist:
            User.objects.create_user(username=username,password=password)
            msg='success'
        return JsonResponse({'msg':msg})
    return render(request,'blog/main.html')

def reset(request):
    if request.method=='POST':
        username,password=(request.body.decode('utf-8')).split('&')
        try:
            user=User.objects.get(username__exact=username)
            user.set_password(password)
            user.save()
            msg='success'
        except:
            msg='error'
        return JsonResponse({'msg':msg})
    return render(request,'blog/main.html')
