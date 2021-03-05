# Generated by Django 3.1.7 on 2021-03-04 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=2)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_in_semester', to='App_Attendance.department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_in_courses', to='App_Attendance.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=255)),
                ('teacher_id', models.CharField(max_length=255)),
                ('submission_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('presence', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_in_attendance', to='App_Attendance.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_in_attendance', to='App_Attendance.department')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_in_attendance', to='App_Attendance.semester')),
            ],
        ),
    ]
