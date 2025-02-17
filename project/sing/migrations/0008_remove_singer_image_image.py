# Generated by Django 5.0.6 on 2024-07-04 16:47

import django.db.models.deletion
import sing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sing', '0007_singer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singer',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=sing.models.image_upload_path)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sing.singer')),
            ],
        ),
    ]
