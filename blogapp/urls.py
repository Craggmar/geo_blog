from django.urls import path

from . import views

app_name = 'blogapp'
urlpatterns = [
    #Home
    path('', views.home, name='home'),
    #Page
    path('<int:page_nr>/', views.index, name='index'),
    #About
    path('about/', views.about, name='about'),
    #Gallery
    path('gallery/', views.gallery, name='gallery'),
     #Gallery
    path('contact/', views.contact, name='contact'),
    #Single Topic
    path('topic/(<int:topic_id>)/', views.topic, name='topic'),
    #New topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #pending
    path('pending_topics/', views.pending_topics, name='pending_topics'),
    path('confirm_topic/(<int:topic_id>)', views.confirm_topic, name='confirm_topic'),
    #List
    path('my_topics/', views.my_topics, name='my_topics'),
    #Edit topic
    path('edit_topic/(<int:topic_id>)/', views.edit_topic, name='edit_topic'),
    #Delete
    path('delete_topic/(<int:topic_id>)/', views.delete_topic, name='delete_topic'),
    #add image
    path('add_image/(<int:topic_id>)/', views.add_image, name='add_image'),
     #About
    path('terms/', views.terms, name='terms'),
    #search
    path('search_topic/', views.search_topic, name='search_topic') 
]
