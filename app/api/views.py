from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)


from app.models import (Faculty,)


from .serializer import (FacultySerializer,)


from rest_framework import permissions

from django.http import HttpResponse
import os
import logging
from django.conf import settings
from django.shortcuts import render


index_file_path = os.path.join(
    settings.BASE_DIR, "app", "static", "app", "index.html")


def index(request):
    try:
        return render(request, "index.html")
        # return render(request, index_file_path)
    except FileNotFoundError:
        logging.exception('Production build of app not found')
        return HttpResponse(
            status=501,
        )


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    # permission_classes = (permissions.AllowAny, )
    permission_classes = (permissions.IsAuthenticated, )


class FacultyDetailView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.AllowAny, )


class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.AllowAny, )


class FacultyUpdateView(UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.AllowAny, )


class FacultyDeleteView(DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.AllowAny, )
