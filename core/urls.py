from django.urls import path
from .views import *
urlpatterns=[
    path('',Home.as_view(),name="home"),
    path('add-student/',Add_student.as_view(),name='add-student'),
    path('delete-student/',delete_Student.as_view(),name='delete-student'),
]