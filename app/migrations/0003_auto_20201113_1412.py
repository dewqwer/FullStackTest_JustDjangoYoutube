# Generated by Django 3.1.1 on 2020-11-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_timemajor_detailid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='queueFacultyPassed',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='university',
        ),
        migrations.RemoveField(
            model_name='major',
            name='queueMajorPassed',
        ),
        migrations.AlterField(
            model_name='countrealtime',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='countrealtime',
            name='round',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='facultyName',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='peopleInFaculty',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='queueFaculty',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='graduationdetail',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='graduationdetail',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graduationdetail',
            name='round',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='major',
            name='majorName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='major',
            name='peopleInMajor',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='major',
            name='queueMajor',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='major',
            name='typeDegree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timemajor',
            name='speed',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NOT OK', 'NOT OK')], max_length=100, null=True),
        ),
    ]
