class Person:
-lastIDUsed = 100
	def __init__(self, tmpFname, tmpLname):
		self._fName = tmpFname
		self._lName = tmpLname
		self._ID = Person._lastIDUsed
		Person._lastIDUsed += 1

	def __str__(self):
		tmp = ""
		tmp += "Last ID Used: " + " " + str(self._lastIDUsed) + " " +\
                        "First Name: " \  str(self._fName) + " " + \
                         "Last Name: " + " " + str(self._lName)
		return tmp

