# Generated by Django 4.2.5 on 2023-11-29 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_alter_student_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_marks', to='vege.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
