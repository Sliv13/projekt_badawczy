from django.urls import path
from . import views

urlpatterns=[
    
    path('answers/submit/',views.submit_answers,name="answers"),
    path('peopleCounter/',views.get_people_number,name="peopleCounter")
]