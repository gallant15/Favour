from django.urls import path
from web.views import home, hello, call, newstudent, school



urlpatterns = [
    path('', home, name="homepage"),
    path('greet/<str:name>', hello),
    path('student', call),
    path('new_student', newstudent, name="back"),
    path('AAUA', school, name="akoko")
]