from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import RegistrationView,LoginView,LogoutView,ForgotPasswordCompleteVies,ForgotPasswordVies, ChangePasswordView
from django.contrib.auth import get_user_model

class AuthTest(APITestCase):
    def setUp(self):
        self.factory= APIRequestFactory()
        self.user = get_user_model().objects.create_user(email='user@gmail.com', password='121311', is_active=True, activation_code='1234')

    def test_registration(self):
        data = {
            'email': 'new_user@gmail.com' ,
            'password': '121311',
            'password_confirm': '121311',
            'name':'Misha',
            'last_name':'Mishanya'
        }
        request = self.factory.post('api/v1/register/', data, format='json')
        print(request)
        view = RegistrationView.as_view()
        response=view(request)
        print(response)

        # assert response.status_code==200
        # assert get_user_model().objects.filter(email=data['email']).exists()

    def test_login(self):
        data = {
            'email': 'user@gmail.com',
            'password':'121311',
        }
        request = self.factory.post('api/v1/account/login/', data, format='json')
        view = LoginView.as_view()
        response=view(request)
        # assert response.status_code==200
        # assert get_user_model().objects.filter(email=data['email']).exists()
        print(response.data)
        assert 'token' in response.data

    def test_change_password(self):
        data ={
            'old_password':'121311',
            'new_password':'727375',
            'new_password_confirm':'727375',
        }
        request = self.factory.post('api/v1/account/change_pas/',data, format='json')
        force_authenticate(request, user=self.user)
        view = ChangePasswordView.as_view()
        response=view(request)
        print(response)
        assert response.status_code==200
