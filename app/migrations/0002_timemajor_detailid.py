# Generated by Django 3.1.1 on 2020-10-28 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timemajor',
            name='detailID',
            field=models.OneToOneField(db_column='graduation_detail_detailID', default='', on_delete=django.db.models.deletion.CASCADE, to='app.graduationdetail'),
            preserve_default=False,
        ),
    ]