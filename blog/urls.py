from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView, \
    toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('article/', cache_page(30)(ArticleListView.as_view()), name='article'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/edit/<int:pk>/', cache_page(30)(ArticleDetailView.as_view()), name='article_edit'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
