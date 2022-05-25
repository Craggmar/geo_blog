from django.urls import path

from . import views

app_name = 'blogapp'
urlpatterns = [
    #Home
    path('', views.index, name='index'),
    #About
    path('about/', views.about, name='about'),
    #Gallery
    path('gallery/', views.gallery, name='gallery'),
    #Single Topic
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
    #New topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #Edit topic
    path('edit_topic/(<int:topic_id>)/', views.edit_topic, name='edit_topic'),
    #Delete
    path('delete_topic/(<int:topic_id>)/', views.delete_topic, name='delete_topic'),
    #add image
    path('add_image/(<int:topic_id>)/', views.add_image, name='add_image'),
    
]
