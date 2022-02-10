from django.http import Http404
from django.views.generic import ListView, DetailView
from articles.models import Article


class IndexView(ListView):
    """
    Articles List View
    """
    template_name = "index.html"
    queryset = Article.objects.all()


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



