from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()



class Exercises(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Workouts(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(to=Exercises, through='WorkoutsExercises') #string cuz gets defined later
    date = models.DateField(auto_now_add=True)


class WorkoutsExercises(models.Model):
    workout = models.ForeignKey(to=Workouts, on_delete=models.CASCADE)
    exercise = models.ForeignKey(to=Exercises, on_delete=models.CASCADE)

    sets = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    repetitions = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])