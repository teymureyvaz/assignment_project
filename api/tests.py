from django.test import Client
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


class PostStatisticsByPostIdTests(APITestCase):
    def test_get_post_successfull(self):
        data = [{"user_id": 111,"post_id": 232,"likes_count": 34}]
        url = reverse('store')
        self.client.post(url, data, format='json')
        response = self.client.get('/post/statistics_by_post_id/232')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_failure(self):
        data = [{"user_id": 111, "post_id": 232, "likes_count": 34}]
        url = reverse('store')
        self.client.post(url, data, format='json')
        response = self.client.get('/post/statistics_by_post_id/22')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class  PostStatisticsByUserIdTests(APITestCase):
    def test_get_post_by_user_successfull(self):
        data = [{"user_id": 111,"post_id": 232,"likes_count": 34}]
        url = reverse('store')
        self.client.post(url, data, format='json')
        response = self.client.get('/post/statistics_by_user_id/111')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_by_user_failure(self):
        data = [{"user_id": 111, "post_id": 232, "likes_count": 34}]
        url = reverse('store')
        self.client.post(url, data, format='json')
        response = self.client.get('/post/statistics_by_user_id/22')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
