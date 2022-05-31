from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

import os
import shutil


from .models import Topic, Image
from .forms import CommentForm, TopicForm, ImageForm


def index(request):
    topics = Topic.objects.order_by('-date_created')
    context = {'topics': topics}
    return render(request, 'blogapp/index.html', context)


def about(request):
    return render(request, 'blogapp/about.html')


def gallery(request):

    # folders_dirs= []
    # all_images_dirs = []
        
    # for root, dirs, files in os.walk(settings.MEDIA_ROOT):
    #     for dir in dirs:
    #         folders_dirs.append(os.path.join(root, dir))
    
    # for folder in folders_dirs:
    #     for root, dirs, files in os.walk(folder):
    #         for file in files:
    #             all_images_dirs.append(os.path.join(root, file))

    all_images = Image.objects.all()


    '''Tymczasowy test'''
    # all_images = []

    # topics = Topic.objects.all()
    # for topic in topics:
    #     all_images.append(topic.header_image)
    
                
    context={"images":all_images}
    return render(request, 'blogapp/gallery.html',context)


def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    comments = topic.comment_set.order_by('-date_created')
    images = topic.image_set.all()

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
   
    context = {
        'topic': topic, 'comments': comments, 'form': form,'images':images,
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
            if not new_topic.title in os.listdir(settings.MEDIA_ROOT):
                os.mkdir(os.path.join(settings.MEDIA_ROOT, new_topic.title))
            
                pass
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
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, topic.title))
        return redirect('blogapp:index')

    context = {'topic':topic}
    
    return render(request, 'blogapp/delete_topic.html', context)


@login_required
def add_image(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form= ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:
            new_image = form.save(commit=False)
            new_image.topic= topic
            new_image.save()
            return redirect('blogapp:topic', topic_id=topic.id)
    context = {'topic':topic, 'form':form}
    return render(request, 'blogapp/add_image.html', context)
