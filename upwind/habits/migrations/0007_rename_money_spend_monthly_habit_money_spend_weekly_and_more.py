# Generated by Django 4.0.3 on 2022-04-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_alter_habit_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='money_spend_monthly',
            new_name='money_spend_weekly',
        ),
        migrations.RenameField(
            model_name='habit',
            old_name='time_spend_monthly',
            new_name='time_spend_weekly',
        ),
        migrations.AddField(
            model_name='habit',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
