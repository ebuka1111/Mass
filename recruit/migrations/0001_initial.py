# Generated by Django 4.2.7 on 2023-11-30 22:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('home_address', models.CharField(max_length=300)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('ssn', models.CharField(max_length=11, unique=True, verbose_name='Social Security Number')),
                ('id_document', models.CharField(choices=[('DL', "Driver's License"), ('PP', 'Passport'), ('SID', 'State ID')], max_length=100)),
                ('Images', models.ImageField(default='DEFAULT VALUE', upload_to='Documents')),
                ('former_workplace', models.CharField(blank=True, max_length=200, null=True)),
                ('workplace_address', models.TextField(blank=True, null=True)),
                ('reason_for_leaving', models.TextField(blank=True, null=True)),
            ],
        ),
    ]