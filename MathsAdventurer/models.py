from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class User(AbstractUser):
    pass

class Competition(models.Model):
    name = models.CharField(max_length=50)
    min_grade = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    max_grade = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    runner = models.CharField(max_length=25)
    website = models.URLField(max_length=100)
    rounds = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    users_watching = models.ManyToManyField(User, blank=True, related_name="watchlist")
    def __str__(self):
        return f"{self.name}({self.rounds})"
    
class Event(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="events")
    date = models.DateField()
    round = models.IntegerField(default=1)
    class written_choices(models.TextChoices):
        ONLINE = 'online'
        CAMPUS = 'at central location'
        SCHOOL = 'at your own school'
    written = models.CharField(choices= written_choices.choices, default=written_choices.ONLINE, max_length=30)
    
class Milestone(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_milestones")
    competition = models.ForeignKey(Competition, on_delete= models.CASCADE, related_name="competition_milestones")
    year = models.IntegerField(default=2023)
    round = models.IntegerField(default=1)
    placement = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    class status_choices(models.IntegerChoices):
        NOTYET = 0,'Not attempted yet'
        MISSED = 1,'Missed milestone'
        ACHIEVED = 2,'Achieved milestone'
    status = models.IntegerField(choices = status_choices.choices, default=status_choices.NOTYET)

class Topic(models.Model):
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length = 200)
    image = models.URLField(max_length = 200)
    def __str__(self):
        return self.name

class Difficulty(models.Model):
    name = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    colour = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}({self.real_name})"
    
class Resource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, related_name='resources')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='resources')
    