from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="players")
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
        return self.user.username

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=255)
    FULL_COURT = 'FC'
    HALF_COURT = 'HC'
    ONE_VS_ONE = 'OO'
    SHOOT_AROUND = 'SA'
    TYPE_CHOICES = [
        (FULL_COURT, 'Full Court: 5 vs 5'),
        (HALF_COURT, 'Half Court: 3 vs 3'),
        (ONE_VS_ONE, 'Half Court: 1 vs 1'),
        (SHOOT_AROUND, 'Shoot Around'),
    ]
    game_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    player = models.ManyToManyField(Player)

    def __str__(self):
        return self.name 
