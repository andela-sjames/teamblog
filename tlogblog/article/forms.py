from django import forms
from models import Article,Comment,Quote


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('author','title','body','pub_date','thumbnail',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name','body','pub_date',)

class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = ('title','body',)
