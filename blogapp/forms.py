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
        fields = ['title', 'description', 'text', 'header_image', 'header_image_description']
        widgets =  {
            'text' : forms.Textarea(attrs={
                'placeholder': 'Aby dodać nagłówek, umieść go między tagami "<h4></h4>". \nTreść umieść pomiędzy tagami "<p></p>"'
                    '\n\nPrzykład:\n\n<h4>Twój nagłówek</h4>\n\n<p>Twoja treść</p>'}),
                'rows': 20,
            'description': forms.Textarea(attrs={'rows':3}),
            
            }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'description', 'image']
        
        
        

