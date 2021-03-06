# Generated by Django 3.1.7 on 2021-03-04 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=120)),
                ('Batch', models.CharField(max_length=30)),
                ('Section', models.CharField(max_length=30)),
                ('Routine_image', models.ImageField(default='/static/image/defaultRoutine.jpg', upload_to='Routine')),
                ('Publish_date', models.DateTimeField(auto_now_add=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Routine_Author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_title', models.CharField(max_length=256)),
                ('Department', models.CharField(max_length=120)),
                ('Batch', models.CharField(max_length=30)),
                ('Section', models.CharField(max_length=30)),
                ('Video', models.FileField(upload_to='Videos')),
                ('Publish_date', models.DateTimeField(auto_now_add=True)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Class_Teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lecture_title', models.CharField(max_length=256)),
                ('Department', models.CharField(max_length=120)),
                ('Batch', models.CharField(max_length=30)),
                ('Section', models.CharField(max_length=30)),
                ('Notes', models.FileField(upload_to='lecture-note')),
                ('Publish_date', models.DateTimeField(auto_now_add=True)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
