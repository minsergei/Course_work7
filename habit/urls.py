from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),

    path('public_habits/', PublicHabitListAPIView.as_view(), name='public-habit-list'),
]
