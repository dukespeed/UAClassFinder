'''
Authors: Duke Speed, Audrey Gagum, Yash Agarwal, Sophie Guinan
'''
import requests
class_search_url = "https://catsched.studentcenter.arizona.edu/nlx7/psc/pubsaprd//UA_SCHEDULE/HRMS/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL"
#class_search_url = "https://studentcenter.arizona.edu/app/ui/public/select-campus" #needs a new request
select_campus_to_search = {'ICAction':'UA_CLAS_SRCH_WK_SSR_PB_SRCH', 'IF-TargetVerb':'POST'}

# WARNING: THIS IS ASSUMING THAT WE HAVE ALREADY SELECTED OUR CAMPUS, AS IS REQUIRED ON THE PUBLIC CLASS SEARCH
search_select_cs = {'ICAction':'CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH', # telling the page we want to submit a search
                   'SSR_CLSRCH_WRK_SUBJECT_SRCH$1':  'CSC', # department the class is under
                   'SSR_CLSRCH_WRK_CATALOG_NBR$3': '120', # class num
                   'IF-TargetVerb':'POST', # submit the search form
                   }


with requests.Session() as s:
    # get to the campus select page, and force the page to load components by trying to access the search.
    select_campus_page = s.post(class_search_url, data=select_campus_to_search)
    # select the main campus.
    class_search_page = s.post(class_search_url, data=select_campus_to_search)
    # search for CSC120 classes
    cs120_sessions = s.post(class_search_url,data=search_select_cs)

    cs = cs120_sessions.text
