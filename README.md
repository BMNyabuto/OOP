# OOP
OOP is a python program that uses Object Oriented mechanisms to prototype a property management system used to lease property on a monthly period and acquire property on a 3 year contract.

#Getting Started
OOP requires a python environment in order to run. In case you do not have python installed in your device, you can download it: https://www.python.org/downloads/
After your python environment is ready, open the file with a text editor and then run it.

#Basic Structure
OOP contains 3 classes: an abstract base class(ABC); Property_Management, and two child classes; Apartment and Maisonettes.  
Property_Management achieves abstraction through ABCMeta and abstractmethod classes from python's abc library. Through these classes, Property_Management establishes ACID properties and also enforces 
reliability through preventing data or operation modifications.

ALso, the child classes exploit inheritance so as to carry out their specific opearations(encapsulation).    

#How to Use
OOP is a python command line program. The following are some examples that will help you get familiar with its operation.

1. Define and initiate an object instance through the suitable child class. 
	e.g. in the case of letting out an apartment to a client for the first time,
			Kili = Apartments('Kilimani', 'YES')
		 
		 in the case of letting out an apartment to a client who lives in that apartment
			Kili = Apartments('Kilimani', None)

2. Carry out an operation that calculates the amount they should pay for that apartment
		i.e Kili.Compute_ToLetPrices()
										output: Returns the amount they should pay based on the contract stage

#Python version
Created in python version 2.7.12