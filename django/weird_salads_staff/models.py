from django.db import models


class Staff(models.Model):
    name = models.TextField()
    location = models.IntegerField()
    date_of_birth = models.DateField()
    iban = models.TextField()
    bic = models.TextField()

    def __str__(self) -> str:
        return self.name
