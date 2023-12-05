from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
ID_DOCUMENT_CHOICES = [
        ('DL', 'Driver\'s License'),
        ('PP', 'Passport'),
        ('SID', 'State ID'),
    ]

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    home_address = models.CharField(max_length=300)
    phone_number = PhoneNumberField()
    ssn = models.CharField(max_length=11, unique=True, verbose_name="Social Security Number")
    id_document = models.CharField(max_length=100, choices=ID_DOCUMENT_CHOICES)
    Images = models.ImageField(upload_to="Documents", blank=True, null=True)
    former_workplace = models.CharField(max_length=200, blank=True, null=True)
    workplace_address = models.TextField(blank=True, null=True)
    reason_for_leaving = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
