from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, PostStatistics


class PostCreateTests(APITestCase):
    def test_create_post_successfull(self):
        url = reverse('store')
        data = [{"post_id": 2, "user_id": 134, "likes_count": 5},{"post_id": 2, "user_id": 134, "likes_count": 5}]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_failure(self):
        url = reverse('store')
        data = [{"user": 134, "post_id": 2, "likes_count": 5}]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
