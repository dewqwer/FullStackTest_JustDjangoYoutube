from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)


from app.models import (Major,)


from .serializer import (MajorSerializer,)


from rest_framework import permissions

from django.http import HttpResponse
import os
import logging
from django.conf import settings
from django.shortcuts import render


index_file_path = os.path.join(settings.BASE_DIR, "static", "app")


def index(request):
    try:
        return render(request, index_file_path)
    except FileNotFoundError:
        logging.exception('Production build of app not found')
        return HttpResponse(
            status=501,
        )


class MajorListView(ListAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (permissions.AllowAny, )
    # permission_classes = (permissions.IsAuthenticated, )


class MajorDetailView(RetrieveAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (permissions.AllowAny, )


class MajorCreateView(CreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (permissions.AllowAny, )


class MajorUpdateView(UpdateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (permissions.AllowAny, )


class MajorDeleteView(DestroyAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (permissions.AllowAny, )
