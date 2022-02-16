from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin, FormView

from articles.forms import NewArticleForm
from articles.models import Article, Writer


class IndexView(ListView):
    """
    Articles List View
    """
    template_name = "index.html"
    queryset = Article.objects.all()
    paginate_by = 12


class ArticleDetails(DetailView):
    """
    Selected Article details View
    """
    template_name = 'article_details.html'
    queryset = Article.objects.all()

    def get_object(self, *args, **kwargs):
        """
        Get Article by pk(id)
        """
        article_id = self.kwargs.get("pk")
        try:
            article = Article.objects.get(id=article_id)
            return article
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            return Article.objects.filter(pk=article_id).first()

@login_required(login_url="login")
def create_new_article(request):
    writer = Writer.objects.get(user=request.user)
    form = NewArticleForm(request.POST or None, initial={"writer": writer})

    if form.is_valid():
        title = form.cleaned_data["title"]
        text = form.cleaned_data["text"]
        cover = form.cleaned_data["cover"]
        writer = form.cleaned_data["writer"]
        article = Article.objects.create(title=title, text=text, cover=cover, writer=writer)
        article.save()

    context = {
        "form": form
    }
    return render(request, "article_create.html", context)

