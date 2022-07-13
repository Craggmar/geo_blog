from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    #Home
    path('', views.api, name='api'),
    path('get_topics/', views.get_topic, name='get_topic'),
    path('add_topic/', views.add_topic, name='add_topic'),        
]