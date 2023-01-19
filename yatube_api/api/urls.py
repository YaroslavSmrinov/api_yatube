from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupsViewSet, PostViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(
    r'users',
    UserViewSet,
    basename='users')
router.register(
    r'posts',
    PostViewSet,
    basename='posts')
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments')
router.register(
    r'groups',
    GroupsViewSet,
    basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
