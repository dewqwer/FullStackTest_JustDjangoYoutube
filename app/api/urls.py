from django.urls import path, include

from .views import (FacultyCreateView,
                       FacultyDeleteView,
                       FacultyDetailView,
                       FacultyListView,
                       FacultyUpdateView,
                       )





app_name = 'todo-api'
urlpatterns = [

    path('', FacultyListView.as_view(),name='list'),
    # path('faculty/', FacultyListView.as_view(),name='list'),
    path('faculty/<pk>', FacultyDetailView.as_view()),
    path('faculty/add/', FacultyCreateView.as_view()),
    path('faculty/<pk>/update/', FacultyUpdateView.as_view()),
    path('faculty/<pk>/delete/', FacultyDeleteView.as_view()),




]