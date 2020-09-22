from django.urls import path

from .views import (FacultyListView,
                    FacultyDetailView,
                    FacultyCreateView,
                    FacultyDeleteView,
                    FacultyUpdateView)

urlpatterns = [
    path('', FacultyListView.as_view()),
    path('create/', FacultyCreateView.as_view()),
    path('<pk>', FacultyDetailView.as_view()),
    path('<pk>/update/', FacultyUpdateView.as_view()),
    path('<pk>/delete/', FacultyDeleteView.as_view())


]
