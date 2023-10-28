from django.db import models



class Food(models.Model):
    name = models.CharField(max_length=60)
    serving_size = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    kcal = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carb = models.IntegerField()

    def __str__(self):
        return self.name
    