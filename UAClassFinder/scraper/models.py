from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    class_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)

    # section = models.CharField(max_length=10)
    # days = models.CharField(max_length=10)
    # time = models.CharField(max_length=10)
    # location = models.CharField(max_length=100)
    # status = models.CharField(max_length=10)
    # seats = models.CharField(max_length=10)
    # waitlist = models.CharField(max_length=10)
    # credit = models.IntegerField()
    # restrictions = models.CharField(max_length=100)

    def __str__(self):
        return self.course_id + " " + self.course_name
