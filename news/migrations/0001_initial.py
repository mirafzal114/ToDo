# Generated by Django 4.2.2 on 2023-06-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('name_task', models.CharField(max_length=200, verbose_name='name task')),
                ('task_txt', models.TextField(max_length=2000, verbose_name='task text')),
                ('date', models.DateTimeField(verbose_name='enter time')),
            ],
        ),
    ]
