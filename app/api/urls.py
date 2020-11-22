from django.urls import path, include

from .views import (FacultyCreateView,
                    FacultyDeleteView,
                    FacultyDetailView,
                    FacultyListView,
                    FacultyUpdateView,
                    )

from .views import index

from django.conf import settings
from django.conf.urls.static import static


app_name = 'todo-api'
urlpatterns = [
    path('', index, name="index"),

    path('api/faculty/', FacultyListView.as_view(), name='list'),
    # path('faculty/', FacultyListView.as_view(),name='list'),
    path('api/faculty/<pk>', FacultyDetailView.as_view()),
    path('api/faculty/add/', FacultyCreateView.as_view()),
    path('api/faculty/<pk>/update/', FacultyUpdateView.as_view()),
    path('api/faculty/<pk>/delete/', FacultyDeleteView.as_view()),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
