from datetime import date
from django.shortcuts import render

from .models import Topic

def index(request):
    topics = Topic.objects.order_by('date_created')
    context = {'topics': topics}
    return render(request, 'blogapp/index.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    comments = topic.comment_set.order_by('-date_created')
    context = {'topic': topic, 'comments': comments}
    return render(request, 'blogapp/topic.html', context)
    
