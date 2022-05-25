from django import forms

from .models import Topic, Comment, Image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets =  {'text' : forms.Textarea(attrs={'rows': 10, 'cols':60},)}

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'text', 'header_image']
        labels = {'text': ''}

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'description', 'image']
        labels = {'text': '', 'image':''}
        

