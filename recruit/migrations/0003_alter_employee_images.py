# Generated by Django 4.2.7 on 2023-12-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0002_alter_employee_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Images',
            field=models.ImageField(blank=True, null=True, upload_to='Documents'),
        ),
    ]
