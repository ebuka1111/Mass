from django.contrib import admin
from .models import Employee

# Register your models here.

class adminEmployee(admin.ModelAdmin):
    list_display = ["first_name","last_name", "home_address", "ssn"]
    list_filter = ["first_name", "home_address"]
    search_fields = ["first_name", "last_name", "home_address", "ssn"]
admin.site.register(Employee, adminEmployee)


