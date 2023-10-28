# Generated by Django 4.2.6 on 2023-10-22 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]