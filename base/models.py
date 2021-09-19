from django.db import models

# Create your models here.

class client(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname

class order(models.Model):
    client = models.ForeignKey(client, on_delete = models.CASCADE)
    type = models.CharField(max_length=15)
    weight = models.IntegerField()

    def __str__(self):
        return self.type
