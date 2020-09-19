from django.db import models

# Create your models here.


class Faculty(models.Model):
    facultyID = models.AutoField(primary_key=True)
    facultyName = models.CharField(max_length=40)
    peopleInFaculty = models.PositiveIntegerField()
    university = models.CharField(max_length=40)
    queueFaculty = models.PositiveIntegerField()
    queueFacultyPassed = models.BooleanField(null=True)

    def __str__(self):
        return "{} {}".format(self.facultyID, self.facultyName)

    class Meta:
        db_table = "faculty"


class Major(models.Model):
    majorID = models.AutoField(primary_key=True)
    typeDegree = models.CharField(max_length=40)
    majorName = models.CharField(max_length=40)
    peopleInMajor = models.PositiveIntegerField()
    queueMajor = models.PositiveIntegerField()
    queueMajorPassed = models.BooleanField(null=True)
    facultyID = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, db_column='faculty_facultyID')

    # self ขึ้นสีแดง แต่ว่า code run ได้ปกติ ไม่รู้ทำไม
    def __str__(self):
        return "{} {}".format(Faculty.__str__(self.facultyID), self.majorName)

    class Meta:
        db_table = "major"


class timeMajor(models.Model):
    timeID = models.AutoField(primary_key=True)

    # ยังไม่รู้ว่าจะ time stramp โดยใช้เวลาในเครื่องที่ run อยู่ยังไง
    timeStart = models.TimeField(null=True, blank=True)
    timeStop = models.TimeField(null=True, blank=True)
    timeExpect = models.TimeField(null=True, blank=True)
    #

    requireMeanTime = models.PositiveIntegerField(null=True)
    speed = models.CharField(max_length=40, choices=[(
        'OK', 'OK'), ('NOT OK', 'NOT OK')], null=True, blank=True)
    majorID = models.ForeignKey(
        Major, on_delete=models.CASCADE, null=True, db_column='major_majorID')

    def __str__(self):
        return Major.__str__(self.majorID)

    class Meta:
        db_table = "time_major"


class GraduationDetail(models.Model):
    detailID = models.AutoField(primary_key=True)
    academinYear = models.PositiveIntegerField()

    # ยังไม่รู้ว่าจะ date stramp โดยใช้เวลาในเครื่องที่ run อยู่ยังไง + ยังไม่ได้กำหนดรูปแบบ d-m-y กับฝั่ง Programming
    date = models.DateField()

    typeCeremony = models.BooleanField()
    round = models.PositiveIntegerField(null=True)
    place = models.CharField(max_length=40, null=True, blank=True)
    facultyID = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, db_column='faculty_facultyID')

    # ขึ้นสีแดง แต่ว่า code run ได้ปกติ ไม่รู้ทำไม
    def __str__(self):
        return "{} {} {}".format("ปีการศึกษา", self.academinYear, Faculty.__str__(self.facultyID))

    class Meta:
        db_table = "graduation_detail"


class CountRealTime(models.Model):
    countID = models.AutoField(primary_key=True)

    # ยังไม่รู้ว่าจะ date stramp โดยใช้เวลาในเครื่องที่ run อยู่ยังไง + ยังไม่ได้กำหนดรูปแบบ d-m-y กับฝั่ง Programming
    date = models.DateField()

    round = models.PositiveIntegerField(null=True)
    peopleCount = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = "count_real_time"
