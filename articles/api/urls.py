from django.urls import path

from .views import FacultyListView, FacultyDetailView

urlpatterns = [
    path('', FacultyListView.as_view()),
    path('<pk>', FacultyDetailView.as_view),


]
