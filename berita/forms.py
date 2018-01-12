from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', ]


class PostForm(forms.ModelForm):

    # featured = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Post
        fields = [
            'title',
            'post_pic',
            'embed',
            'body',
            'status',
            'tags',
            'featured',
        ]
