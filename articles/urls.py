from django.urls import path
from .views import *

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/new_comment/', CommentCreateView.as_view(), name='comment_new'),
]
