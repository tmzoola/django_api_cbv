from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index),
    path('students/',views.StudentList.as_view()),
    path('students/<int:pk>',views.StudentDetail.as_view()),

]