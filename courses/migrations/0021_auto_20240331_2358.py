# Generated by Django 3.1.14 on 2024-03-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('courses', '0020_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='preferred_courses',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_users', to='auth.Group', verbose_name='groups'),
        ),
    ]
