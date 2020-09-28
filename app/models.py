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
