from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)


from app.models import (Faculty,)

from app.models import (Major,)

from app.models import (QueueManagement,)


from .serializer import (FacultySerializer,)


from .serializer import (FacultyJoinMajorSerializer,)

from .serializer import (MajorJoinQueueManagementSerializer,)


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
    permission_classes = (permissions.AllowAny, )
    # permission_classes = (permissions.IsAuthenticated, )


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

class FacultyJoinMajorListView(ListAPIView):
    test=Major.objects.select_related('facultyID')
    print(test.query)

    queryset = Faculty.objects.all()
    print(queryset)
    serializer_class = FacultyJoinMajorSerializer
    permission_classes = (permissions.AllowAny, )

class MajorJoinQueueManagementListView(ListAPIView):
    test=QueueManagement.objects.select_related('majorID')
    print("majorJaaaa::: ",test.query)

    queryset = Major.objects.all()
    print(queryset)
    serializer_class = MajorJoinQueueManagementSerializer
    permission_classes = (permissions.AllowAny, )
