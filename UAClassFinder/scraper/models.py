from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    section_id = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)
    instructors = models.CharField(max_length=100)
    days_week = models.CharField(max_length=100)
    time = models.TimeField()                       # Takes a time, can change to char
    open_class = models.CharField(max_length=1)     # A Y/N arguement for now
    start_date = models.DateField()
    end_date = models.DateField()
    modularity = models.CharField(max_length=100)
    last_update = models.DateTimeField()    

    def __str__(self):
        #was originally 
        #return self.course_id + " " + self.course_name 
        return self.section_id + " " + self.class_name    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_courses = models.ManyToManyField(Course)
    

    def __str__(self):
        return self.user.username