class Person:
-lastIDUsed = 100
def __init__(self, tmpFname, tmpLname):
self._fName = tmpFname
self._lName = tmpLname
self._ID = Person._lastIDUsed
Person._lastIDUsed += 1

