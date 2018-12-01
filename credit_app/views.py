from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import site_users

def index(request):
    return render(request, 'credit_app/index.html') 

def users_table(request):
    all_users = site_users.objects.all()
    return render(request, 'credit_app/users_table.html', { 'all_users' : all_users })

def user_info(request, user_id):
    user = get_object_or_404(site_users,pk=user_id)
    return render(request, 'credit_app/user_info.html',{ 'user' : user })

def credit_transfer(request, user_id):
    user = get_object_or_404(site_users, pk=user_id)
    to_user = site_users.objects.filter(username__startswith=request.POST['to_user'])
    to_user=list(to_user)[0]
    credits = request.POST['credits']
    if int(credits)<=user.credits:
        to_user.credits+=int(credits)
        user.credits-=int(credits)
        user.num_transactions+=1
        user.save()
        to_user.save()
        return render(request, 'credit_app/successful.html', { 'user' : user })
    else:
        return render(request, 'credit_app/unsuccessful.html', { 'error_message' : 'You do not have enough credits to make this transaction' } )

