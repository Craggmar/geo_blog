from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from users.decorators import allowed_users

import os
import shutil


from .models import Topic, Image
from .forms import CommentForm, TopicForm, ImageForm

def home(request):
    return redirect ('/0/')

def index(request, page_nr):
    all_topics = Topic.objects.filter(confirmed=True).order_by('-date_created')
    topics = all_topics[1:]
    last_topic = all_topics[0]

    numbers_of_topic_for_single_page = 6
    tpp = numbers_of_topic_for_single_page
     
    if len(topics) - (page_nr * tpp + tpp) >= 0:
        visible_topics = topics[page_nr*tpp : page_nr*tpp+tpp]
    elif len(topics) - (page_nr * tpp + tpp) < tpp > 0:
        visible_topics = topics[page_nr*tpp : ]

    class Page():
        def __init__(self) -> None:
            self.nr = page_nr
            self.last_nr = int(len(topics) / (tpp))
            self.next_nr = self.nr + 1
            if self.nr >0:
                self.prev_nr = self.nr - 1
            else:
                self.prev_nr = 0
    
    
    page = Page()

    context = {'topics': visible_topics, 'last_topic':last_topic, 'page': page,}
    return render(request, 'blogapp/index.html', context)


def about(request):
    return render(request, 'blogapp/about.html')

def terms(request):
    return render(request, 'blogapp/terms.html')


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
    # topic = Topic.objects.get(id = topic_id)
    topic =    get_object_or_404(Topic, id=topic_id)
    comments = topic.comment_set.order_by('-date_created')
    images = topic.image_set.all()

    #Add new comment form
    if request.method != 'POST':
        form = CommentForm()
    else:
        print('prev')
        form = CommentForm(data=request.POST)
        print('postval')
        if form.is_valid():
            new_comment = form.save(commit=False)
            print('false')
            new_comment.topic = topic
            print('topic')
            new_comment.owner = request.user
            print('user')
            new_comment.save()
            print('full')
        return redirect('blogapp:topic', topic.id)
   
    context ={'topic': topic, 'comments': comments, 'form': form,'images':images,}
    return render(request, 'blogapp/topic.html', context)

def my_topics(request):    
    topics = Topic.objects.filter(owner=request.user).order_by('-date_created')
    
    context = {'topics': topics,}
    return render(request, 'blogapp/my_topics.html', context)


@login_required
@permission_required('blogapp.add_topic', raise_exception=True)
# @allowed_users(allowed = ['admins', 'moderators'])
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner= request.user
            new_topic.save()
            if not new_topic.title in os.listdir(settings.MEDIA_ROOT):
                os.mkdir(os.path.join(settings.MEDIA_ROOT, new_topic.title))
            return redirect('blogapp:home')

    context = {'form': form}

    return render(request, 'blogapp/new_topic.html', context)


@login_required
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        form= TopicForm(instance=topic)
    else:
        form = TopicForm(request.POST, request.FILES, instance=topic)
        if form.is_valid:
            form.save()
            return redirect('blogapp:topic', topic_id=topic.id)

    context = {'topic':topic, 'form':form}

    return render(request, 'blogapp/edit_topic.html', context)


@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method =='POST':
        topic.delete()
        if  topic.title in os.listdir(settings.MEDIA_ROOT):                
            shutil.rmtree(os.path.join(settings.MEDIA_ROOT, topic.title))
        return redirect('blogapp:home')

    context = {'topic':topic}
    
    return render(request, 'blogapp/delete_topic.html', context)


@login_required
def add_image(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        form= ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:             
            checkbox_value = request.POST.get('show_in_gallery')
            new_image = form.save(commit=False)
            if not checkbox_value:
                new_image.show_in_gallery = False
            new_image.topic= topic
            new_image.save()
            return redirect('blogapp:topic', topic_id=topic.id)
    context = {'topic':topic, 'form':form}
    return render(request, 'blogapp/add_image.html', context)
