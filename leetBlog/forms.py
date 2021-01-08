from django import forms
from .models import Comments,Post


class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','comment')

        widgets = {
            'name': forms.TextInput(),
            'comment': forms.Textarea()
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post     
        fields = ('title', 'author' , 'content') 

        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput({'id':'author', 'value':'','type':'hidden'}),
            'content': forms.Textarea()
        }   
class PostForm(forms.ModelForm):
    class Meta:
        model = Post     
        fields = ('title', 'author' , 'content') 

        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput({'id':'author', 'value':'','type':'hidden'}),
            'content': forms.Textarea()
        }           