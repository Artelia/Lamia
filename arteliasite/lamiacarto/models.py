from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Project(models.Model):
    id_projet = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    postgisdb = models.CharField(max_length=255)
    postgisuser = models.CharField(max_length=255)
    postgispw = models.CharField(max_length=255)
    qgisserverurl = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="users")

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "projet"

