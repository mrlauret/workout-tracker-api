from rest_framework import serializers
from .models import Workouts, Exercises, WorkoutsExercises


class WorkoutsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workouts
        fields = ['id', 'name']

class ExercisesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercises
        fields = ['id', 'name']

class WorkoutsExercisesSerializer(serializers.ModelSerializer):
    workout = serializers.PrimaryKeyRelatedField(read_only=True)
    exercise = ExercisesSerializer(read_only=True)
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercises.objects.all(), 
        source='exercise', 
        write_only=True
    )
    
    class Meta:
        model = WorkoutsExercises
        fields = ['id', 'workout', 'exercise', 'exercise_id','sets', 'repetitions']