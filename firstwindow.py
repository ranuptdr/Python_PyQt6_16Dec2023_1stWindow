import sys # sys is a built-in module in python
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QWidget

# classobject = ClassName()
# Creating an instance/object of QApplication
ranu = QApplication([]) # []passing am empty list, ranu is a external clas object
win = QWidget()  # win  is a external clas object,   Creating an instance of QWidget

# Setting the window title
win.setWindowTitle("Ranupatidar")


# classobject.method()
win.show() 
ranu.exec()