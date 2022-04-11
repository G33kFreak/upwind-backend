# Generated by Django 4.0.3 on 2022-04-10 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relapse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(max_length=255)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relapses', to='habits.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]