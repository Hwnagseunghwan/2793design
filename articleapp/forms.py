from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all()) #(<-, required=False) Project 목록에서 항목을 선택하지 않아도 되는 옵션

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']