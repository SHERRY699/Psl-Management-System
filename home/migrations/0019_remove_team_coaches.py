# Generated by Django 4.2.2 on 2023-07-15 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_coaches_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='coaches',
        ),
    ]