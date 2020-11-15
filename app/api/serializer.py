from rest_framework.serializers import(
    HyperlinkedIdentityField,
    ModelSerializer
)

from app.models import Faculty


class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
