import imp
from django.urls import URLPattern, path
from api import views



urlpatterns = [
    path('student/' , views.StudentList.as_view()),
]