# Generated by Django 4.0.3 on 2022-03-28 19:43

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
                ('time_spend_monthly', models.FloatField(blank=True, default=None)),
                ('money_spend_monthly', models.FloatField(blank=True, default=None)),
                ('user', models.UUIDField(editable=False)),
            ],
        ),
    ]