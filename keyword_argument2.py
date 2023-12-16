#1. Function Defination is one time process
def hello(std1,std2): # formal argument, def is a keyword
    print(f'Hello {std1} and {std2}')
    pass

#2. Function Calling/invoking is many time process
hello("Ranu",'kushal') # Actual argument

# hello(key=value)
hello(std2="Ranu", std1='kushal') # Keyword Argument
