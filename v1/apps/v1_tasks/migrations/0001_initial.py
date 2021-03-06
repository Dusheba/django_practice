# Generated by Django 3.2.3 on 2021-05-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('v1_lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_points', models.IntegerField(verbose_name='maximum points')),
                ('min_points', models.IntegerField(verbose_name='minimum points for passing')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1_lessons.lesson')),
            ],
        ),
    ]
