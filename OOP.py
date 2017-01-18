from abc import ABCMeta, abstractmethod

class Property_Management(object):
	"""Property Renting and To Let Services"""
	__metaclass__ = ABCMeta
	
	Deposit = 0
	No_of_Rooms = 0
	
	def __init__(self, location, Availability_Status):
		"""Return a new Car Object"""
		self.location = location            
		self.Availability_Status = Availability_Status
		