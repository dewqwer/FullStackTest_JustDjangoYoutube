from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Faculty
from .serializers import FacultySerializer


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetailView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
