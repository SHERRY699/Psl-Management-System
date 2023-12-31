# Generated by Django 4.2.2 on 2023-07-15 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_player_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='coaches/')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='coach',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.coach'),
            preserve_default=False,
        ),
    ]
