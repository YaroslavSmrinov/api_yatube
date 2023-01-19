from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupsViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(
    r'posts',
    PostViewSet,
    basename='posts')
v1_router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments')
v1_router.register(
    r'groups',
    GroupsViewSet,
    basename='groups')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
