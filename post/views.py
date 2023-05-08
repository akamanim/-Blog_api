from rest_framework import generics, filters
from .models import Category, Tag, Post, Comment
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer, CommentCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'body']


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = CommentCreateSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        elif self.request.method == 'GET':
            return CommentSerializer
