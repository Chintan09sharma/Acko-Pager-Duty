from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Developer(models.Model):

    name = models.CharField(max_length=64)
    mobile = models.BigIntegerField(
        validators=[MinValueValidator(5000000000), MaxValueValidator(9999999999), ],
        db_index=True,
        null=False,
        unique=True
    )

    class Meta:
        db_table = "dummy_developer"

    def __str__(self):
        return self.name


class TeamDeveloperMap(models.Model):

    team_name = models.CharField(max_length=64, unique=True)
    developers = ArrayField(models.IntegerField())

    class Meta:
        db_table = "dummy_team"

    def __str__(self):
        return self.team_name
