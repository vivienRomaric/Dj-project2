# Generated by Django 4.0.1 on 2022-01-13 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]