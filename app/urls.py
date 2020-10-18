from django.contrib import admin

from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from .views import UserViewSet, current_user, UserList
# from .views import UserViewSetForCreatingUser, UserViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls.static import static
from .views import index
from app.views import FacultyCreateView, FacultyDeleteView, FacultyDetailView, FacultyListView, FacultyUpdateView

from .views import socket

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),

    path('listall/', FacultyListView.as_view()),
    path('create/', FacultyCreateView.as_view()),
    path('<pk>', FacultyDetailView.as_view()),
    path('<pk>/update/', FacultyUpdateView.as_view()),
    path('<pk>/delete/', FacultyDeleteView.as_view()),
    
    path('showNum/', socket)




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
