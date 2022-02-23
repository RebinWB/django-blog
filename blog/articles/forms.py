from django import forms

from articles.models import Article


class NewArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Title"
    }), label="Title")

    text = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Article Body"
    }), label="Text")


    class Meta:
        model = Article
        fields = ["title", "text", "cover"]

