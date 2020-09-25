from django.contrib import admin

from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import UserViewSet, current_user, UserList
from .views import UserViewSetForCreatingUser, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
