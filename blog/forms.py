from blog.models import Comment, Article
from django import forms

class  CommentsForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('body', 'enable')


class  ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = ('title', 'body', 'is_active', 'category')
