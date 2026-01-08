from django import forms

from load.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields= ['title', 'cover']



