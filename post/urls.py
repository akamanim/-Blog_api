from django.urls import path
from .views import CategoryListView, TagListView, PostListCreateView, PostDetailView, CommentListCreateView


urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('tags/', TagListView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()), 
    path('comments/', CommentListCreateView.as_view()),
]