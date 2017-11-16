import os 

def answer():
	""" 
	Goal = to have the following pattern : "3, Kal. July -> 3 days before kalendes of july"
	"""
	number = int(input("Please insert your number : "))
	feast = str.capitalize(input("Please insert your feast : "))
	month = str.capitalize(input("Please insert your month : "))
	
	return number 
	return feast 
	return month 

def feast():
	"""
	Goal = Input rules for feasts
	"""
	if feast == "Kal" or "Kalendes" or "Kal.":
		return 1
	if feast == "Nones" or "Non" or "Non.":
		if month == "Martius" or "Maius" or "Quinctilis" or "October":
			return 7 
		else:
			return 5
	if feast == "Ides" or "Eid" or "Eid.":
		if month == "Martius" or "Maius" or "Quinctilis" or "October":
			return 15
		else:
			return 13

def roman_month():
	"""
	Goal = To provide nbre of days in months
	"""
	if month == "Ianuarius" or "Martius" or "Maius" or "Quinctilis" or "Iulius" or "Sextilis" or "Augustus" or "October" or "December":
		return 31
	if month == "Aprilis" or "Iunius" or "September" or "November":
		return 30
	if month == "Februarius":
		return 28


answer()

print(number)



os.system("pause")
