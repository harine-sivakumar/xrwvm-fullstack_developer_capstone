from django.db import models

# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car Model Model
class CarModel(models.Model):

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"

    CAR_TYPES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name="models"
    )

    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"