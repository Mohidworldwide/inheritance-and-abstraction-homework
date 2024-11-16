#homework 1


# class parent():
#     def __init__(self,name,idnumber):
#         self.name=name 
#         self.idnumber=idnumber
#     def display (self):
#         print (self.name)
#         print (self.idnumber)
# class child(parent):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         parent.__init__(self,name,idnumber)
# a=child("mohid",9,10000,"principal")
# a.display()

#homework 2
from abc import ABC
class animal(ABC):

    def move(self):
        pass
class human (animal):
    def move (self):
        print ("i can walk")



h=human()
h.move()   


class dog (animal):
    def move (self):
        print ("i can bark")

d=dog()
d.move()