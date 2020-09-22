from rest_framework import permissions
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from articles.models import Faculty
from .serializers import FacultySerializer


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetailView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )


class FacultyUpdateView(UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )


class FacultyDeleteView(DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )
