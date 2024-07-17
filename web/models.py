from django.db import models

# Create your models here.
APPROVED_DEPT= [
    ('APH', 'Animal Science'),
    ('CSC', 'Computer Science'),
    ('MTH', "Mathematics")
]
class Student(models.Model):
    name= models.CharField(max_length=255)
    reg_number= models.CharField(max_length=20, unique= True)
    dept= models.CharField(max_length=30, choices= APPROVED_DEPT, default= APPROVED_DEPT[0] [0])
    age= models.PositiveIntegerField(null= True, blank= True)
    cgpa= models.DecimalField(max_digits= 3, decimal_places= 2)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    def __str__(self):
        return f"{self.name} - {self.reg_number}"
