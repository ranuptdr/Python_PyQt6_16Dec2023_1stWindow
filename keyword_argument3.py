#1. Class Defination 
class Country(): # class is a keyword, ClassName always be in PascalCase Pattern
     #1.1  property  = Variable
    name = ''
    capital = ''
    
    #1.2   construsctor
    # constructor is a special method whose name is __init___ 
    ''' def __init__(self,n,c): # always put first argument as self & n,c is formal argument '''
    def __init__(self,c,n): # always put first argument as self & n,c is formal argument
        # self is internal object
        self.name = n  # The role of constructor is To initialize the property 
        self.capital = c  #  The role of constructor is To initialize the property 

    #1.3   Method/Function (functionName always be in camelCase Pattern)
    def displayCountryDetail(self):  # always put first argument as self, self is internal object
        print(f'{self.capital} is the Capital Of {self.name}')
    pass

#2. create class object/create instance of the class
# classobject = ClassName()
''' ceo = Country('India',"Delhi") # ceo is a external clas object '''
ceo = Country(n='India',c="Delhi") # Keyword Argument, ceo is a external clas object

# classobject.method()
ceo.displayCountryDetail()