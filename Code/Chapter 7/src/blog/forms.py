from django import forms

from blog.models import Blog
from blog.models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog

        fields = [
            'title'
        ]

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost

        fields = [
            'title',
            'body'
        ]