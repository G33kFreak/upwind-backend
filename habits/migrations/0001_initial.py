# Generated by Django 4.0.3 on 2022-04-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('time_spend_weekly', models.FloatField(blank=True, default=None)),
                ('money_spend_weekly', models.FloatField(blank=True, default=None)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
