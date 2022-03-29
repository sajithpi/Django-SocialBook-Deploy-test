# Generated by Django 3.2 on 2022-02-03 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0017_auto_20220203_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chat',
            name='content',
            field=models.CharField(default=0, max_length=1555, null=True),
        ),
    ]
