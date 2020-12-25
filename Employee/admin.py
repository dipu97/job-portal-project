from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','company_name','email','phone']
    list_editable = ['name','email','phone','company_name']
    list_per_page = 25
    list_filter = ['company_name']



# Register your models here.
admin.site.register(Employee,EmployeeAdmin)