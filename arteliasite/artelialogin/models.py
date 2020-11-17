from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    pghost = models.CharField(max_length=255, blank=True)
    pgport = models.IntegerField(blank=True)
    pgdbname = models.CharField(max_length=255, blank=True)
    pgschema = models.CharField(max_length=255, blank=True)
    pguser = models.CharField(max_length=255, blank=True)
    pgpassword = models.CharField(max_length=255, blank=True)

    qgisserverurl = models.CharField(max_length=255, blank=True)
    users = models.ManyToManyField(User, related_name="users", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"

