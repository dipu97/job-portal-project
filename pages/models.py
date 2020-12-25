from django.db import models

# Create your models here.
class Contact(models.Model):
    message=models.TextField(verbose_name="Message",null=True)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    report_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name