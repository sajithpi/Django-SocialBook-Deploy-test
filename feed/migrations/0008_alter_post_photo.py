# Generated by Django 3.2.9 on 2021-12-15 05:08

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]
