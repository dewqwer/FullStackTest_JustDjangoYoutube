from rest_framework.serializers import(
    HyperlinkedIdentityField,
    ModelSerializer
)

from app.models import Major


class MajorSerializer(ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'
