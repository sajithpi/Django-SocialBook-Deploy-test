# Generated by Django 3.2 on 2022-02-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0023_chat_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='receiver',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='sender',
            field=models.CharField(max_length=55),
        ),
    ]
