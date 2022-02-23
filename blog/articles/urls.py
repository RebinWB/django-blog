from django.urls import path

from articles.views import IndexView, ArticleDetails, create_new_article, WriterArticlesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/<pk>/<slug>/', ArticleDetails.as_view(), name='blog_details'),
    path('new/', create_new_article, name="new_article"),
    path('author/<pk>/<username>/', WriterArticlesView.as_view(), name="writer_articles")
]



