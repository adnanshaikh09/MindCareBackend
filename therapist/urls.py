from django.urls import path
from .views import DoctorListView

urlpatterns = [
    path("therapist/", DoctorListView.as_view(),name='therapist-list'),
]