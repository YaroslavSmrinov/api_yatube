from posts.models import Group, Post, User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthor
from .serializers import (CommentSerializer, GroupSerializer, PostSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.select_related('author', 'group')
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        pk = self.kwargs.get('post_id')
        post = Post.objects.get(pk=pk)
        serializer.save(author=post.author, post=post)

    def get_queryset(self):
        pk = self.kwargs.get('post_id')
        post = Post.objects.get(pk=pk)
        queryset = post.comments.all()

        return queryset
