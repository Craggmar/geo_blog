from django.shortcuts import render,redirect 

from django.contrib.auth import login, logout
from django.contrib.auth.models import Group, User
from django.conf import settings

from users.decorators import unauthenticated_user
from .forms import CreateUserForm, EditUserProfileForm, CreateUserForm
from.models import BlogUser
from blogapp.models import Comment, Topic

from.decorators import unauthenticated_user

import os

def register(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method !="POST":
        form = CreateUserForm()
    else:
        form = CreateUserForm(data=request.POST)       
        
        if form.is_valid():
            new_user= form.save()
            permissions = request.POST.get('permissions')
            group = Group.objects.get(name = permissions)
            new_user.groups.add(group)
            BlogUser.objects.create(user=new_user, name=new_user.username, email=new_user.email, permission_group=permissions)

            login(request, new_user)
            return redirect('blogapp:home')    

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def logged_out(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})

def user_account(request):
    bloguser = request.user.bloguser
    if request.method != 'POST':        
        form = EditUserProfileForm(instance=bloguser)
    else:
        form = EditUserProfileForm(request.POST, request.FILES, instance=bloguser)      
        if form.is_valid:
            if request.FILES:
                if "default_user.png" not in bloguser.profile_picture.url:
                    os.remove(os.path.join(settings.MEDIA_ROOT, str(bloguser.profile_picture)))
            form.save()
    context = {'form': form}
    return render(request, 'user/user_account.html', context)

def view_account(request, username):
    user = User.objects.get(username=username)
    comments = Comment.objects.filter(owner=user)
    topics = Topic.objects.filter(owner=user)
    comments_amount = len(comments)
    topics_amount = len(topics)

    context = {'user':user, 'comments_amount':comments_amount, 'topics_amount':topics_amount}
    return render(request, 'user/view_account.html', context)




        







