# Generated by Django 4.2.7 on 2023-11-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Images',
            field=models.ImageField(upload_to='Documents'),
        ),
    ]
