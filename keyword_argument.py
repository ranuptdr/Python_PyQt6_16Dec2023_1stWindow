#1. Function Defination is one time process
def hello(std='Tanisha'): # formal argument, def is a keyword, std is default argumment
    print(f'Hello {std}')
    pass

#2. Function Calling/invoking is many time process
hello("Ranu") # Actual argument
hello('Tannu') # Actual argument
hello() # calling function without argument
