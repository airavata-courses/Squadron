from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

# Create your tests here.

# Test Serializer
from api.serializers import UserSerializer

from api.views import RegisterUserView


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_attributes = {
            'first_name': 'abc',
            'last_name': 'xyz',
            'username': 'abc_xyz',
            'email': 'abc@xyz.com',
            'password': 'Password@1'
        }

        self.serialize_data = {
            'first_name': 'abc',
            'last_name': 'xyz',
            'username': 'abc_xyz_test',
            'email': 'abc@xyz.com',
            'password': 'Password@1'
        }

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)
        self.factory = APIRequestFactory()
        self.registerUserView = RegisterUserView.as_view({'post': 'create'})

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['first_name', 'last_name', 'email', 'username']))
        # Make sure password is not returned as it is a write-only field
        self.assertFalse(('password' in data.keys()))

    def test_serializer_contains_expected_content(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user_attributes['username'])
        self.assertEqual(data['first_name'], self.user_attributes['first_name'])
        self.assertEqual(data['last_name'], self.user_attributes['last_name'])
        self.assertEqual(data['email'], self.user_attributes['email'])

        # Make sure password is not returned as it is a write-only field
        self.assertFalse(('password' in data.keys()))

    def test_deserializer_works_correctly(self):
        request = self.factory.post('/api/register', self.serialize_data)
        response = self.registerUserView(request=request).render()
        # 201 status means CREATED
        self.assertEquals(201, response.status_code)

    def test_deserializer_duplicate_username_not_allowed(self):
        request = self.factory.post('/api/register', self.user_attributes)
        response = self.registerUserView(request=request).render()
        # 400 as the user is already created during the setup
        self.assertEquals(400, response.status_code)
