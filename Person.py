class Person:
-lastIDUsed = 100

def __str__(self):
tmp = ""
tmp += "Last ID Used: " + " " + str(self._lastIDUsed) + " " + "First Name: " \
       str(self._fName) + " " + "Last Name: " + " " + str(self._lName)
return tmp

