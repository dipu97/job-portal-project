from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="photos/%y/%m/%d")
    company_name=models.CharField(max_length=250,blank=False,verbose_name="Company")
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    cv=models.FileField(upload_to="pdf/%y/%m/%d")
    message=models.TextField(blank=True,verbose_name="Message")
    contact_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name