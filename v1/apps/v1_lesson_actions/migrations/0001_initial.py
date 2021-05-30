# Generated by Django 3.2.3 on 2021-05-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('v1_materials', '0001_initial'),
        ('v1_users', '0001_initial'),
        ('v1_lessons', '0001_initial'),
        ('v1_tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_points', models.IntegerField(verbose_name='user_points')),
                ('mark', models.IntegerField(verbose_name='user_mark')),
                ('material_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('task_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('lesson_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('last_lesson', models.ManyToManyField(blank=True, null=True, related_name='last_lesson', to='v1_tasks.Task')),
                ('last_task', models.ManyToManyField(blank=True, null=True, related_name='last_task', to='v1_tasks.Task')),
                ('lesson', models.ManyToManyField(blank=True, null=True, related_name='lesson_action', to='v1_lessons.Lesson')),
                ('listener', models.ManyToManyField(related_name='lesson_action_user', to='v1_users.User')),
                ('material', models.ManyToManyField(blank=True, null=True, related_name='material_action', to='v1_materials.Material')),
                ('task', models.ManyToManyField(blank=True, null=True, related_name='task_action', to='v1_tasks.Task')),
            ],
        ),
    ]
