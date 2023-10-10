from django import forms

from blog.models import Article
from service.forms import StyleFromMixin


class ArticleForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('quantity', 'sign',)
