from django.urls import path

from . import views

app_name = 'blogapp'
urlpatterns = [
    #Home
    path('', views.index, name='index'),
    #Single Topic
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),

]
