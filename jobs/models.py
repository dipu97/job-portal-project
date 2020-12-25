from django.db import models

# Create your models here.
from django.db import models
from Employee.models import Employee
# Create your models here.
class jobs(models.Model):
    Employee=models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=250)
    position=models.CharField(max_length=200)
    nature=models.CharField(max_length=200)
    salary=models.CharField(max_length=150)
    job_type=models.CharField(max_length=150)
    location=models.CharField(max_length=250)
    category=models.CharField(max_length=200)
    logo=models.ImageField(upload_to="photos/logo/%y/%m/%d")
    experience=models.CharField(max_length=200)
    expired_date=models.DateTimeField(auto_now_add=False)
    qualification=models.TextField()
    gender=models.CharField(max_length=50)
    is_published=models.BooleanField()
    vacency=models.DecimalField(decimal_places=0,max_digits=4)
    published_date=models.DateTimeField(auto_now_add=False)
    update=models.DateTimeField(auto_now_add=True,null=True)
    responsibilities = models.TextField()
    benefit = models.TextField()




    def __str__(self):
        return self.title
    class Meta:
        ordering=('-published_date',)


class application(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=25)
    link=models.CharField(max_length=150)
    cv=models.FileField()
    cover=models.TextField()

    def __str__(self):
        return self.name
