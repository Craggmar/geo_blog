from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from users.decorators import allowed_users

import os, shutil

from .models import Topic, Image
from .forms import CommentForm, TopicForm, ImageForm

def home(request):
    return redirect ('/0/')

def index(request, page_nr):
    all_topics = Topic.objects.filter(confirmed=True).order_by('-date_created')
    try:
        last_topic = all_topics[0]
    except IndexError:
        last_topic = None
        
    try:
        topics = all_topics[1:]
    except IndexError:
        topics = []
    

    numbers_of_topic_for_single_page = 6
    tpp = numbers_of_topic_for_single_page
     
    if len(topics) - (page_nr * tpp + tpp) >= 0:
        visible_topics = topics[page_nr*tpp : page_nr*tpp+tpp]
    elif len(topics) - (page_nr * tpp + tpp) < tpp > 0:
        visible_topics = topics[page_nr*tpp : ]

    class Page():
        def __init__(self) -> None:
            self.nr = page_nr
            self.last_nr = int(len(topics) / (tpp+1))
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
    all_images = Image.objects.all()    
                
    context={"images":all_images}
    return render(request, 'blogapp/gallery.html',context)

def search_topic(request):
    all_topics = Topic.objects.filter(confirmed=True).order_by('-date_created')
    topics = []
    if request.method == 'POST':
        searched = request.POST['searched']
        for topic in all_topics:
            if searched.lower() in topic.title.lower():
                topics.append(topic)
    context ={'topics': topics, 'searched':searched}
    return render(request, 'blogapp/search_topic.html', context)

def topic(request, topic_id, image_id=None):
    topic =    get_object_or_404(Topic, id=topic_id)
    comments = topic.comment_set.order_by('-date_created')
    images = topic.image_set.all()

    #Add new comment form
    if request.method != 'POST':
        form = CommentForm()
    else:
        if image_id:
            redirect ('blogapp:delete_image', topic_id, image_id)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = topic
            new_comment.owner = request.user
            new_comment.save()        
   
    context ={'topic': topic, 'comments': comments, 'form': form,'images':images,}
    return render(request, 'blogapp/topic.html', context)

@login_required
def my_topics(request):    
    # topics = Topic.objects.filter(owner=request.user).order_by('-date_created')
    topics = request.user.topic_set.order_by('-date_created')
    
    context = {'topics': topics,}
    return render(request, 'blogapp/my_topics.html', context)

@login_required
@permission_required('is_staff', raise_exception=True)
def pending_topics(request):
    topics = Topic.objects.filter(confirmed=False).order_by('-date_created')
    
    context = {'topics': topics,}
    return render(request, 'blogapp/pending_topics.html', context)

@login_required
@permission_required('is_staff', raise_exception=True)
def confirm_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method =='POST':        
        topic.confirmed = True
        topic.save()
    return redirect('blogapp:pending_topics')

@login_required
@permission_required('blogapp.add_topic', raise_exception=True)
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner= request.user
            new_topic.save()
            # create media dir
            if not new_topic.title in os.listdir(settings.MEDIA_ROOT):
                os.mkdir(os.path.join(settings.MEDIA_ROOT, new_topic.title))
            return redirect('blogapp:home')

    context = {'form': form}
    return render(request, 'blogapp/new_topic.html', context)


@login_required
@permission_required('blogapp.edit_topic', raise_exception=True)
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        form= TopicForm(instance=topic)
    else:
        form = TopicForm(request.POST, request.FILES, instance=topic)
        if form.is_valid:
            form.save()
            return redirect('blogapp:topic', topic.id)

    context = {'topic':topic, 'form':form}

    return render(request, 'blogapp/edit_topic.html', context)


@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method =='POST':
        topic.delete()
        #del media dir
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


def delete_image(request, topic_id, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('blogapp:topic', topic_id)
