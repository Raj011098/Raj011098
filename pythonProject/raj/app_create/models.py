from django.db import models

class ether(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.BigIntegerField()



    def __str__(self) -> str:
        return self.firstname