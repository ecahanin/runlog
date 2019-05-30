from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_lenght=20)
    model = models.CharField(max_length=20)
    date_purchased = models.DateField()
    #add image to shoes

    def __str__(self):
        return self.name


class Run(models.Model):
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DurationField()
    pace = models.DurationField()
    notes = models.TextField(blank=True)
    race = models.BooleanField(default=False)
    datetime = models.DateTimeField()
    