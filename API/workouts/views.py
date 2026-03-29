from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import WorkoutsSerializer, ExercisesSerializer, WorkoutsExercisesSerializer
from .models import Workouts, Exercises, WorkoutsExercises

#add exercise to workout

class WorkoutsListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutsSerializer

    def get_queryset(self):
        return Workouts.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WorkoutsDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutsSerializer

    def get_queryset(self):
        return Workouts.objects.filter(owner=self.request.user)

class ExercisesListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExercisesSerializer

    def get_queryset(self):
        return Exercises.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ExercisesDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExercisesSerializer

    def get_queryset(self):
        return Exercises.objects.filter(owner=self.request.user)

class WorkoutsExercisesListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutsExercisesSerializer

    def get_queryset(self):
        workout_owned_by_user = Workouts.objects.get(owner=self.request.user, id=self.kwargs['pk'])
        exercises_in_workout = WorkoutsExercises.objects.filter(workout=workout_owned_by_user)

        return exercises_in_workout
    
    def perform_create(self, serializer):
        workout_owned_by_user = Workouts.objects.get(owner=self.request.user, id=self.kwargs['pk'])

        serializer.save(workout=workout_owned_by_user)

class WorkoutsExercisesDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutsExercisesSerializer

    def get_queryset(self):
        workout_owned_by_user = Workouts.objects.get(owner=self.request.user, id=self.kwargs['workout_pk'])
        
        return WorkoutsExercises.objects.filter(workout=workout_owned_by_user)