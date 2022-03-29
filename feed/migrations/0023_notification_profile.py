# Generated by Django 3.1 on 2022-01-20 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20220120_2018'),
        ('feed', '0022_auto_20220120_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
