from django.urls import path, include
from .views import CategoryListView, TagListView,  CommentViewSet, PostViewSet, RatingView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('rating', RatingView)

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('tags/', TagListView.as_view()),
    # path('posts/', PostViewSet.as_view({'get': 'list'})),
    # path('posts/', PostViewSet.as_view({'post': 'create'}))
    path('', include(router.urls) )
    # path('', include(router.urls))

    
]