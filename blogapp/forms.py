from django import forms

from .models import Topic, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets =  {'text' : forms.Textarea(attrs={'lenght': 200})}

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'text']
        labels = {'text': ''}

