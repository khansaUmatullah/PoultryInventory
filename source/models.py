from django.db import models


# Create your models here.
### CASE STUDY 1. Models

class Chicken(models.Model):
    Health_Status_Choices=[("Healthy","Healthy"),
                           ("Sick", "Sick"),
                           ("Deceased", "Deceased"),]
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    breed=models.CharField(max_length=50)
    health_status=models.CharField(max_length=10,choices=Health_Status_Choices)
    def __str__(self):
        return self.name


class Egg(models.Model):
    chicken=models.ForeignKey(Chicken,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_collected=models.DateField()




