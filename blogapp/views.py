from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.settings import BASE_DIR
import os
import shutil

from .models import Topic
from .forms import CommentForm, TopicForm

PROJECT_PATH = os.path.abspath(os.path.dirname('blog'))
IMG_PATH= os.path.join(PROJECT_PATH, 'static/images/')


def index(request):
    topics = Topic.objects.order_by('date_created')
    context = {'topics': topics}
    return render(request, 'blogapp/index.html', context)

def about(request):
    return render(request, 'blogapp/about.html')

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    comments = topic.comment_set.order_by('-date_created')
    #change comment date format
    for comment in comments:
        comment.date_created = comment.date_created.strftime('%m-%d-%y; %H:%M')

    #Show last topic change date string
    if topic.date_modified > topic.date_created:
        last_change_date_str =  'Ostatnio zmodyfikowano: '+ topic.date_modified.strftime('%m-%d-%y o %H:%M')
    else:
        last_change_date_str =  'Utworzono: '+ topic.date_created.strftime('%m-%d-%y o %H:%M')
    
    #Add new comment form
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = topic
            new_comment.owner = request.user
            new_comment.save()
        return redirect('blogapp:topic', topic.id)

    #Image list links
    images = os.listdir('static/images/'+topic.title)
    imgs_list_dir = [IMG_PATH+topic.title+'/'+img for img in images]
    


    context = {
        'topic': topic, 'comments': comments, 'form': form, 'date':last_change_date_str,'images':imgs_list_dir,
         }
    return render(request, 'blogapp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner= request.user
            new_topic.save()
            path= os.getcwd()
            os.mkdir(IMG_PATH+new_topic.title)
            return redirect('blogapp:index')

    context = {'form': form}

    return render(request, 'blogapp/new_topic.html', context)

@login_required
def edit_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form= TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogapp:topic', topic_id=topic.id)
    context = {'topic':topic, 'form':form}
    return render(request, 'blogapp/edit_topic.html', context)

@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method =='POST':
        topic.delete()
        shutil.rmtree(IMG_PATH+topic.title)
        return redirect('blogapp:index')

    context = {'topic':topic}
    
    return render(request, 'blogapp/delete_topic.html', context)

        


    
