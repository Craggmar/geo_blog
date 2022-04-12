from datetime import date
from django.shortcuts import render, redirect

from .models import Topic
from .forms import CommentForm, TopicForm

def index(request):
    topics = Topic.objects.order_by('date_created')
    context = {'topics': topics}
    return render(request, 'blogapp/index.html', context)

def about(request):
    return render(request, 'blogapp/about.html')

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    comments = topic.comment_set.order_by('-date_created')

    #Show last change date and string
    if topic.date_created == topic.date_modified:
        last_change_date_str =  'Utworzono: '+ topic.date_created.strftime('%m-%d-%y; %H:%M')
    else:
        last_change_date_str = 'Ostatnio zmodyfikowano: '+ topic.date_modified.strftime('%m-%d-%y; %H:%M') 

    #Add new comment form
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = topic
            new_comment.save()

    context = {
        'topic': topic, 'comments': comments, 'form': form, 'last_change_date_str': last_change_date_str
        }


    return render(request, 'blogapp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:index')

    context = {'form': form}

    return render(request, 'blogapp/new_topic.html', context)

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

def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method =='POST':
        topic.delete()
        return redirect('blogapp:index')

    context = {'topic':topic}
    return render(request, 'blogapp/delete_topic.html', context)

        


    
