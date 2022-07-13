from django.shortcuts import render,redirect 

from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib import messages

from users.decorators import unauthenticated_user
from .forms import CreateUserForm

from.decorators import unauthenticated_user


@unauthenticated_user
def register(request):  

    if request.method !="POST":
        form = CreateUserForm()
    else:
        form = CreateUserForm(data=request.POST)       
        
        if form.is_valid():
            new_user= form.save()
            permissions = request.POST.get('permissions')
            group = Group.objects.get(name = permissions)
            new_user.groups.add(group)
            login(request, new_user)
            return redirect('blogapp:home')    

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def logged_out(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})




        







