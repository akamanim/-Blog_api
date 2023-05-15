from django.contrib.auth import get_user_model
from .models import Post, Tag, Category
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from .views import PostViewSet
User = get_user_model()

class PostTset(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title='cat1')
        tag = Tag.objects.create(title='tag1')
        self.tags = (tag, )
        user = get_user_model().objects.create_user(email='user@gmail.com',password='12345', is_active=True, name='test')
        self.token='12345'
        posts = [
            Post(author=user, body='new_post1', title='post1', category=self.category),
            Post(author=user, body='new_post2', title='post2', category=self.category)
        ]
        Post.objects.bulk_create(posts)

    def test_list(self):
        request = self.factory.get('api/v1/posts/')
        view = PostViewSet.as_view({'get':'list'})
        response = view(request)
        # print(response)
        assert response.status_code == 200

    # def test_create(self):
    #     data = {
    #         'tag':'tag2',
    #         # 'title': 'cat1',
    #         # 'body': 'new_post1',
    #         'category': 'cat2'
    #     }
    #     request = self.factory.post('api/v1/posts/', data, format='json')
    #     view = PostViewSet.as_view({'post': 'create'})
    #     response = view(request)

    #     assert response.status_code == 200

    # def test_update(self):
    #     data = {
    #         'category': 'cats',
    #         'tag': 'tags'
    #     }
    #     request = self.factory.post('api/v1/posts/', data, format='json')
    #     view = PostViewSet.as_view({'put': 'update'})
    #     response = view(request)

    #     assert response.status_code == 200


    # def test_delete(self):
    #     data = {
    #         '':''
    #     }
    #     request = self.factory.get('api/v1/posts/', data, format='json')
    #     view = PostViewSet.as_view({'delete': 'destroy'})
    #     response = view(request)

    #     assert response.status_code == 200


    def test_retrieve(self):
        id = Post.objects.all()[0].id
        request = self.factory.get(f'/posts/{id}/')
        view = PostViewSet.as_view({'get':'retrieve'})
        response = view(request, pk=id)

        assert response.status_code == 200


    def test_create(self):
        user = get_user_model().objects.all()[0]
        data = {
            'body': 'test',
            'title': 'post11',
            'category': 'cat1',
            'tags':['tag1']
        }
        request = self.factory.post('/posts/', data, format='json')
        force_authenticate(request, user=user, token=self.token)
        view = PostViewSet.as_view({'post': 'create'})
        responce = view(request)
        # print(responce)

        assert responce.status_code == 201


    def test_update(self):
        user = User.objects.all()[0]
        data = {
            'body': 'updated body',
            
        }
        post = Post.objects.all()[1]
        request = self.factory.patch(f'/posts/{post.id}/', data, format='json')
        force_authenticate(request, user=user, token=self.token)
        view = PostViewSet.as_view({'patch':'partial_update'})
        responce = view(request, pk=post.id)
        # print(responce.data)

        assert Post.objects.get(id=post.id).body == data['body']


    def test_delete(self):
        user = User.objects.all()[0]
        post = Post.objects.all()[0]
        request = self.factory.delete(f'/posts/{post.id}/')
        force_authenticate(request, user)
        view = PostViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk = post.id )
        print(response.status_code)

        assert response.status_code==204
        assert not Post.objects.filter(id=post.id).exists()