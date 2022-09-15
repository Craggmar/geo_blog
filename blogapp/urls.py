from django.urls import path

from . import views

app_name = 'blogapp'
urlpatterns = [
    #Home
    path('', views.home, name='home'),
    path('<int:page_nr>/', views.index, name='index'),

    #Sites
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('terms/', views.terms, name='terms'),

    #Topic
    path('topic/(<int:topic_id>)/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('edit_topic/(<int:topic_id>)/', views.edit_topic, name='edit_topic'),
    path('delete_topic/(<int:topic_id>)/', views.delete_topic, name='delete_topic'),

    #topics lists
    path('pending_topics/', views.pending_topics, name='pending_topics'),
    path('confirm_topic/(<int:topic_id>)', views.confirm_topic, name='confirm_topic'),
    path('my_topics/', views.my_topics, name='my_topics'),
     
    #Images
    path('add_image/(<int:topic_id>)/', views.add_image, name='add_image'),
    path('delete_image/(<int:topic_id>-<int:image_id>)/', views.delete_image, name='delete_image'),

    #search
    path('search_topic/', views.search_topic, name='search_topic') ,
]
