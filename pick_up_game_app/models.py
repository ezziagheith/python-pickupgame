from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=18)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience = models.PositiveIntegerField(default=0)
    PG = 'PG'
    SG = 'SG'
    SF = 'SF'
    PF = 'PF'
    C = 'C'
    POSITION_CHOICES = [
        (PG, 'Point Guard'),
        (SG, 'Shooting Guard'),
        (SF, 'Small Forward'),
        (PF, 'Power Forward'),
        (C, 'Center'),
    ]
    pref_position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    

    def __str__(self):
        return self.name



