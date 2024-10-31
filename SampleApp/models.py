from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    class_div = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name