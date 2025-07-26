#class 1
class Canada():
    def capital(self):
        print("Ottawa is the capital of Canada")
        
    def language(self):
        print("English and French is the most widely spoken language of Canada.")
        
    def type(self):
        print("Canada is a developed country")
        

#class 2
class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA")
        
    def language(self):
        print("English is the primary language of USA")
        
    def type(self):
        print("USA is a developed country")
        
#object creation
obj_cad= Canada()
obj_usa = USA()

#common interface
for country in (obj_cad, obj_usa):
    country.capital()
    country.language()
    country.type()