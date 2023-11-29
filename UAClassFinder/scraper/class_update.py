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
    #OR delete database. W/e

    #Determine if Fall or Spring Semester, to update accordingly
    semester = "00"
    if(string_to_parse=="01"):
        #Set to Fall/Winter Semester
        semester = "01"
    else:
        #Set to Spring/Summer Semester
        semester = "02"
    #If something went wrong and semester is not set to
    #either Fall or Spring, exit function
    '''
    if(semester=="00"):
        return
    '''
    #Start of loop?
    #Splits data into 2: Useless junk (kinda) and relevent class info
    test00 = string_to_parse.split("classSectionData")
    #Splits relevent class info into each class to parse
    test01 = test00[1].split("instructionMode\":\"Instruction Mode\"")
    #test02 will hold the class title from the search. TODO Change to apply to all classes?
    test02 = ""
    #.find() will find the place in the string to parse
    temp = string_to_parse.find("title")
    #Add by the .find() string's length
    i = temp + 8
    #Iterate through string to get substring
    while temp != -1 and string_to_parse[i] != "\"":
        test02 = test02 + string_to_parse[i]
        i = i + 1
    #Print for testing
    #print(test02 + " classes avaliable: " + str(len(test01) - 1))
    #i for looking at each class. Set to 1 because the items at 0 hold no relevant information
    i = 1

    #Iterate through all classes to store
    while(i<len(test01)):
        #Finds data in string for each class
        #Set substring to a variable called parse
        parse = test01[i]
        #Initialize all strings
        section_id = ""
        class_name = test02     #This one was found earlier TODO Check like above
        instructors = ""
        days_week = ""
        time = ""
        open_class = ""
        start_date = ""
        end_date = ""
        modularity = ""
        #j for iteration
        j = 0

        #Finding sectionID
        temp = parse.find("classNbr")
        if temp != -1:      #If -1, doesn't exist. Error
            j = temp + 11   #Add by the string length of "classNbr"
            while parse[j] != "\"":         #Go until hit end of relevant data (surrounded by quotations)
                section_id = section_id + parse[j]
                j = j + 1
            j = 0
        #print("section_id: " + section_id)

        #Done above (maybe. TODO Check)
        #print("class_name: " + class_name)

        #Finding instructors TODO Check if works with multiple instructors
        temp = parse.find("instructor\":\"<ul><li>")
        if temp != -1:
            j = temp + 21
            while parse[j] != "<":
                instructors = instructors + parse[j]
                j = j + 1
            j = 0
        #print("instructors: " + instructors)

        #Finding both days and times
        temp = parse.find("daysTimes\":\"<ul><li>")
        if temp != -1:
            j = temp + 20
            while parse[j] != " ":
                days_week = days_week + parse[j]
                j = j + 1
            j = j + 1
            while parse[j] != "<":
                time = time + parse[j]
                j = j + 1
            j = 0
        #print("days_week: " + days_week)
        #print("time: " + time)
            
        #Finding status
        temp = parse.find("status\"")
        if temp != -1:
            j = temp + 7
            while parse[j] != "\"":
                open_class = open_class + parse[j]
                j = j + 1
            j = 0
        #print("open_class: " + open_class)

        #Finding start and end times
        temp = parse.find("startEndDate\":\"<ul><li>")
        if temp != -1:
            j = temp + 23
            while parse[j+1] != "-":
                start_date = start_date + parse[j]
                j = j + 1
            j = j + 3
            while parse[j] != "<":
                end_date = end_date + parse[j]
                j = j + 1
            j = 0
        #print("start_date: " + start_date)
        #print("end_date: " + end_date)

        #Finding modularity
        temp = parse.find("instructionMode\":\"")
        if temp != -1:
            j = temp + 18
            while parse[j] != "\"":
                modularity = modularity + parse[j]
                j = j + 1
            j = 0
        #print("modularity: " + modularity)

        last_update = datetime.date.today()

        i = i + 1

        #Database adding stuff
        #If class already in database
        if(Course.objects.get(id=section_id).exists()):
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