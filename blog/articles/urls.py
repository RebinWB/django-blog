from django.urls import path

from articles.views import IndexView, ArticleDetails, create_new_article

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/<pk>/<slug>/', ArticleDetails.as_view(), name='blog_details'),
    path('new/', create_new_article, name="new_article")
]



