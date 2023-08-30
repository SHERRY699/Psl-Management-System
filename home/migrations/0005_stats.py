# Generated by Django 4.2.2 on 2023-07-02 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_stadium_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField()),
                ('wickets', models.IntegerField()),
                ('no_of_fours', models.IntegerField()),
                ('no_of_sixes', models.IntegerField()),
                ('no_of_overs', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.player')),
            ],
        ),
    ]