from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import UserViewSet, current_user, UserList
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'user', UserViewSet)
urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('token_auth/', obtain_jwt_token, name='token_auth'),
    path('current_user/', current_user, name='current_user'),
    path('create_user/', CreateUser.as_view(), name='create_user')
]
