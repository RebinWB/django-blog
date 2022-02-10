from django.urls import path

from articles.views import IndexView, ArticleDetails

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/<pk>/<slug>/', ArticleDetails.as_view(), name='blog_details'),
]



