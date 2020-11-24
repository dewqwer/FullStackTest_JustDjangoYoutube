from rest_framework.serializers import(
    HyperlinkedIdentityField,
    ModelSerializer
)

from app.models import Faculty, Major, QueueManagement


class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class MajorSerializer(ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'

class FacultyJoinMajorSerializer(ModelSerializer):
    faculty_major = MajorSerializer(many=True,read_only=True)
    
    class Meta:
        model = Faculty
        fields = '__all__'

class QueueManagementSerializer(ModelSerializer):
    class Meta:
        model = QueueManagement
        fields = '__all__'


class MajorJoinQueueManagementSerializer(ModelSerializer):
    major_queue_management = QueueManagementSerializer(many=True,read_only=True)
    
    class Meta:
        model = Major
        fields = '__all__'

