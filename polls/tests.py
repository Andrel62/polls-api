from rest_framework.test import APITestCase
#from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from polls import apiviews

class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
        'test',
        email='testuser@test.com',
        password='test'
        )
       
    def test_list2(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'
                .format(response.status_code))
