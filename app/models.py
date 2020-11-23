from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# Note that this is different than null. null is purely database-related,
# whereas blank is validation-related. If a field has blank=True,
# form validation will allow entry of an empty value.
# If a field has blank=False, the field will be required.


class Faculty(models.Model):
    facultyID = models.AutoField(primary_key=True)
    facultyName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{} {}".format(self.facultyID, self.facultyName)

    class Meta:
        db_table = "faculty"


class Major(models.Model):
    majorID = models.AutoField(primary_key=True)
    majorName = models.CharField(max_length=100)
    typeDegree = models.CharField(max_length=100)

    facultyID = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, db_column='faculty_facultyID')

    def __str__(self):
        return "{} {} {}".format(Faculty.__str__(self.facultyID), self.typeDegree, self.majorName)

    class Meta:
        db_table = "major"


class GraduationDetail(models.Model):
    detailID = models.AutoField(primary_key=True)
    academicYear = models.PositiveIntegerField()

    # กำหนดรูปแบบเป็น yyyy-mm-dd
    date = models.DateField(null=True)

    typeCeremony = models.BooleanField()
    round = models.PositiveIntegerField(null=True)
    place = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format("ปีการศึกษา", self.academinYear, Faculty.__str__(self.facultyID))

    class Meta:
        db_table = "graduation_detail"


class timeMajor(models.Model):
    timeID = models.AutoField(primary_key=True)

    # '%H:%M:%S', # '14:30:59'
    timeStart = models.TimeField(null=True)
    timeStop = models.TimeField(null=True)
    timeExpect = models.TimeField(null=True)

    requireMeanTime = models.PositiveIntegerField(null=True)
    speed = models.CharField(max_length=100, choices=[(
        'OK', 'OK'), ('NOT OK', 'NOT OK')], null=True, blank=True)

    majorID = models.ForeignKey(
        Major, on_delete=models.CASCADE, null=True, db_column='major_majorID')

    detailID = models.ForeignKey(
        GraduationDetail, on_delete=models.CASCADE, db_column='graduation_detail_detailID')

    def __str__(self):
        return Major.__str__(self.majorID)

    class Meta:
        db_table = "time_major"


class queue_Management(models.Model):
    queueManagementID = models.AutoField(primary_key=True)
    queueMajor = models.PositiveIntegerField(null=True)
    peopleInMajor = models.PositiveIntegerField(null=True)

    majorID = models.ForeignKey(
        Major, on_delete=models.CASCADE, null=True, db_column='major_majorID')

    detailID = models.ForeignKey(
        GraduationDetail, on_delete=models.CASCADE, db_column='graduation_detail_detailID')


class View(models.Model):
    majorID = models.AutoField(primary_key=True)
    majorName = models.CharField(max_length=100)
