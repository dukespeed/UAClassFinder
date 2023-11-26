'''
Authors: Duke Speed, Audrey Gagum, Yash Agarwal, Sophie Guinan
'''
import requests
from .input_filter import filter_cs

class_search_url = "https://catsched.studentcenter.arizona.edu/nlx7/psc/pubsaprd//UA_SCHEDULE/HRMS/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL"
select_campus_to_search = {'ICAction':'UA_CLAS_SRCH_WK_SSR_PB_SRCH', 'IF-TargetVerb':'POST'}

# WARNING: THIS IS ASSUMING THAT WE HAVE ALREADY SELECTED OUR CAMPUS, AS IS REQUIRED ON THE PUBLIC CLASS SEARCH
def find_class_data(dept, class_num):
    search_select_cs = {'ICAction':'CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH', # telling the page we want to submit a search
                    'SSR_CLSRCH_WRK_SUBJECT_SRCH$1':  dept, # department the class is under
                    'SSR_CLSRCH_WRK_CATALOG_NBR$3': class_num, # class num
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

        #edit to implement formatting - Sophie
        cs = filter_cs(cs) #[formatted_str, course_data_dictionary, course_object] (course object likely isnt instantiated properly)

        return cs[0]