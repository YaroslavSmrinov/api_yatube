from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='posts')

    class Meta:
        model = User
        fields = '__all__'
        ref_name = 'ReadOnlyUsers'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        required=False,
        slug_field='username')
    post = serializers.ReadOnlyField(
        read_only=True,
        source='post.pk')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'created', 'post', 'text',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        required=False,
        slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
