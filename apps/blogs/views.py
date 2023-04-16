
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response


import requests
# Create your views here.

from .models import Post, Tag
from .serializers import TagSerializer, PostDetailSerializer, PostSerializer
from .signals import audit_trail_signal


class TagAPI(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticated]


class PostAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created_at")
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        data = self.request.data
        new_post = serializer.save(
            user=self.request.user, title=data["title"], content=data["content"]
        )
        all_posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(all_posts, many=True)
        # audit_trail_signal.send(sender=self.request.user.__class__, request=self.request,
        #                         user=self.request.user, model="Blog", event_category="Blog", method="CREATE", summary="Create a new post")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
