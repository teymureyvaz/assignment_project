import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import DatabaseError, transaction
from .models import Post, PostStatistics
from .serializers import PostSerializer, PostStatisticsSerializer


class PostCreateView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for item in request.data:
                try:
                    with transaction.atomic():
                        post = Post.objects.filter(id=item['post_id']).first()
                        if post is None:
                            post = Post(id=item['post_id'], user_id=item['user_id'])
                            post.save()
                        post_statistics = PostStatistics(post=post, likes_count=item['likes_count'],
                                                         user_id=item['user_id'])
                        post_statistics.save()

                except DatabaseError:
                    Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "{} posts saved successfully".format(len(request.data))},
                        status=status.HTTP_201_CREATED)


class PostStatisticsByPostIdView(APIView):

    def get(self, request, post_id):
        try:
            obj = PostStatistics.objects.filter(post_id=post_id).latest('created_at').__dict__
        except:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostStatisticsSerializer(data=obj)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostStatisticsByUserIdView(APIView):
    def get(self, request, user_id):
        obj = PostStatistics.objects.filter(user_id=user_id)
        if not obj:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostStatisticsSerializer(instance=obj, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
