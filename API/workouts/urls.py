from django.urls import path

from .views import WorkoutsExercisesDeleteView, WorkoutsExercisesListCreateView, WorkoutsDeleteView, WorkoutsListCreateView, ExercisesDeleteView, ExercisesListCreateView

urlpatterns = [
    path('workouts/', WorkoutsListCreateView.as_view(), name='ListCreateWorkouts'),
    path('workouts/<int:pk>/', WorkoutsDeleteView.as_view(), name='DeleteWorkout'),
    path('exercises/', ExercisesListCreateView.as_view(), name='ListCreateExercises'),
    path('exercises/<int:pk>/', ExercisesDeleteView.as_view(), name='DeleteExercise'),
    path('workouts/<int:pk>/exercises/', WorkoutsExercisesListCreateView.as_view(), name='ListCreateWorkoutExercises'),
    path('workouts/<int:workout_pk>/exercises/<int:pk>/', WorkoutsExercisesDeleteView.as_view(), name='DeleteExerciseFromWorkout')
]