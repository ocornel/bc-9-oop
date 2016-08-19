'''
Done as a group and implemented Individually. Group E
    In Group:
        Qusai   Alfaki
        Ogendi  Ruth
        Muthui  Emmanuel
        Biwot   Kevin
        Gaamuwa Samuel
        Cornel  Martin
'''

import time
class Student(object):
    #Instantiation of students
    country = {
        'KE': 'Kenya',
        'NG': 'Nigeria',
        'UG': 'Uganda',
        'TZ': 'Tanzania'
        }
    class_list=[]
    myId=0
    def __init__(self, fName, lName, cc="KE"):  #By default student Country is Kenya, unless given.
        Student.myId+=1                         #student IDs increment whenever a new student is added
        self.id=Student.myId
        self.fName=fName
        self.lName=lName
        self.applcant_country = Student.country[cc]

    def attend_class(self, **kwargs):
        self.loc=kwargs.setdefault('loc','Hogwarts')    #Default location
        self.date=kwargs.setdefault("date", time.strftime("%c"))
        self.teacher=kwargs.setdefault('teacher','alex') #Default Teacher
        Student.class_list.append((self.date,self.fName,self.lName,self.id,self.loc,self.teacher))
      
   
    def specific_day_attendees(self, date=time.strftime("%c")):
        for item in Student.class_list:
            if item[0]==date:
                print(item)