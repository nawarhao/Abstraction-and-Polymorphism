#import necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):
    
    #function to print a value
    def print(self, x):
        print("Passed value: ", x)
        
        #abstract method
    @abstractmethod #this is an abstract method decorator
    def task(self):
        print("we are inside absclass task")
        
        
#create sub class
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
        
#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.task()
test_obj.print(100)