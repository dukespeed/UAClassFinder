'''
Author: Audrey Gagum
Purpose: Takes the information given from the class search
            function and puts it into the database. If the class 
            is already in the database, it updates the data instead.

         Closes all classes before updating, in the case that 
            the class is not offered in the listed semester. 
'''

from django.db import models
from models import Course       #Database to add to
import datetime                 #Needed to fetch the current time

def update_db(string_to_parse):
    #Set all data in database to FULL/NOT OPEN per semester

    #Determine if Fall or Spring Semester, to update accordingly
    semester = "00"
    if(string_to_parse=="Sept"):
        #Set to Fall/Winter Semester
        semester = "01"
    else:
        #Set to Spring/Summer Semester
        semester = "02"
    #If something went wrong and semester is not set to
    #either Fall or Spring, exit function
    if(semester=="00"):
        return
    
    #Start of loop?
    #Initialize strings
    section_id = semester + "update"
    class_name = "update"
    instructors = "update"
    days_week = "update"
    time = models.TimeField()                       # Takes a time, can change to char
    open_class = "Y"     # A Y/N arguement for now
    start_date = models.DateField()
    end_date = models.DateField()
    modularity = "update"
    last_update = datetime.date.today()

    #If class already in database
    if(section_id == (semester + string_to_parse)):
        #Update
        temp = Course.objects.get(id=section_id)
        temp.section_id = section_id
        temp.class_name = class_name
        temp.instructors = instructors
        temp.days_week = days_week
        temp.time = time
        temp.open_class = open_class
        temp.start_date = start_date
        temp.end_date = end_date
        temp.modularity = modularity
        temp.last_update = last_update
        temp.save()

    else:
        #Add course to database
        new_course = Course(
            section_id,
            class_name,
            instructors,
            days_week,
            time,
            open_class,
            start_date,
            end_date,
            modularity,
            last_update
        )
        new_course.save()