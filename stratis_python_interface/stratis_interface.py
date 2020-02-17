#File Name:   stratis_interface.py
#Purpose:     Command line tool to allow a user to interact with the provided data
#Author:      Austin Ramberg
#Date:        February 15, 2020

import json


# Load data from json file to python dictionary

def load_data(filename):
	with open(filename, 'r') as f:
		outDict = json.load(f)
		return outDict

# Write python dictionary to json file

def write_data(data_source, filename):
	with open(filename, 'w') as f:
		json.dump(data_source, f, indent=4, ensure_ascii=False)

# Enter a unit number and return the residents who live in that unit (someone started that
# one for you but it is not returning the correct values and needs your debugging attention)

def get_resident_names(people_list, unit_number):
	residents = []
	for person in people_list:	
		if person['unit'] == unit_number:
			residents.append(person['first_name'] + ' '+ person['last_name'])
	return residents

# Allow a user to input a first name and last name and retrieve any information we have about
# a resident whose name matches that first and last name. That information should include the 
# user's unit, their role(s) on the property, and any devices that the user can control

def get_user_data(first_name, last_name, people_list):
	out_person = None
	for person in people_list:
		if person['first_name'] == first_name and person['last_name'] == last_name:
			out_person = person

	if out_person is None:
		print('A resident with the name supplied was not found at this property.')
	
	return out_person

# print user data to screen

def display_user_data(user_data):
	print ('first name: ' + user_data['first_name'])
	print ('last name: ' + user_data['last_name'])
	print ('unit: ' + user_data['unit'])
	print ('roles: ')
	for role in user_data['roles']:
		print(role)

# Gets all devices in then property that can be that a user can control
# A person may control a device if:
# 1. It is associated with their unit of residence.
# 2. The device is marked as admin_accessible and the user is an admin.

def get_devices(data_source, user_data):
	is_admin = False
	unit = user_data['unit']
	devices = {'thermostats':[], 'lights':[], 'locks':[]}

	for role in user_data['roles']:
		if role == 'Admin':
			is_admin = True

	for thermostat in data_source['devices']['thermostats']:
		if is_admin and thermostat['admin_accessible'] == "true":
			devices['thermostats'].append(thermostat)
		if str(thermostat['unit']) == unit:
			devices['thermostats'].append(thermostat)

	for light in data_source['devices']['lights']:
		if is_admin and light['admin_accessible'] == "true":
			devices['lights'].append(light)
		if str(light['unit']) == unit:
			devices['lights'].append(light)

	for lock in data_source['devices']['locks']:
		if is_admin and lock['admin_accessible'] == "true":
			devices['locks'].append(lock)
		if str(lock['unit']) == unit:
			devices['locks'].append(lock)

	return devices

# Displays all devices in then property that can be that a user can control

def display_devices(devices):
	print('Devices resident can control:')
	print()
	print('thermostats: ')
	for thermostat in devices['thermostats']:
		print('id: ' + str(thermostat['id']))
		print('unit: ' + str(thermostat['unit']))
		print('model: ' + str(thermostat['model']))
		print()
	print()

	print('lights: ')
	for light in devices['lights']:
		print('id: ' + str(light['id']))
		print('unit: ' + str(light['unit']))
		print('model: ' + str(light['model']))
		print()
	print()

	print('locks: ')
	for lock in devices['locks']:
		print('id: ' + str(lock['id']))
		print('unit: ' + str(lock['unit']))
		print('model: ' + str(lock['model']))
		print()
	print()

# Write a function that will allow the user to move in a new resident or move out an old resident. 
# (Don't change the data in property_data.json. Instead copy the new state of the data into a file 
# named `property_data_changes.json`.)

# Move-in new resident and return new dictionary

def move_in(user_data, data_source):
	data_source['people'].append(user_data)
	print('Successfully moved-in resident!')
	return data_source

# Move-out old resident and return new dictionary

def move_out(first_name, last_name, data_source):
	found = False
	for person in data_source['people']:
		if person['first_name'] == first_name and person['last_name'] == last_name:
			data_source['people'].remove(person)
			print('Successfully moved-out resident!')
			found = True
	if not found:
		print('Resident not found at property...')

	return data_source

# Function to disply the main menu in the loop
def display_menu():
	print('\n')
	print('Menu:')
	print('1. Display residents in provided unit number')
	print('2. Get all data for provided resident')
	print('3. Move in resident')
	print('4. Move out resident')
	print('5. Quit the program')		

# Main function

def main():
	# Initialize data
	data_source = load_data('property_data.json')
	people_list = data_source['people']

	# Take in the user's first and last name and only allow program access if the user is an authorized user. 
	# Assume a user is authorized if they have the property role of "Admin". Don't worry about writing additional 
	# logic to authorize the user.
	first_name = input('Please enter your first name: ')
	last_name = input('Please enter your last name: ')
	is_admin = False
	user_data = get_user_data(first_name, last_name, people_list)
	if user_data is not None:
		for role in user_data['roles']:
			if role == 'Admin':
				print('Authorized user.')
				is_admin = True			

	# Main loop
	if is_admin:
		while True:
			display_menu()
			while True:
				try:
					user_input = float(input('Please type the number for the action you wish to perform: '))
					if user_input not in [1,2,3,4,5]:
						print('Your input was a number, but not between 1 and 5. Please try again.')
						continue
					break
				except:
					print('Error: your answer has to be a numeric value between 1 and 5. Try again.')
			print('\n')

			if(user_input == 1): # Display residents in provided unit number
				unit_number = input('Please enter the unit number: ')
				residents = get_resident_names(people_list, unit_number)
				for resident in residents:
					print(resident)

			elif(user_input == 2): # Get all data for provided resident
				first_name = input('Please enter resident first name: ')
				last_name = input('Please enter resident last name: ')
				print()
				user_data = get_user_data(first_name, last_name, people_list)
				if user_data is not None:
					user_devices = get_devices(data_source, user_data)
					display_user_data(user_data)
					display_devices(user_devices)

			elif(user_input == 3): # Move in resident
				user_data = { 'first_name': None,
							  'last_name': None,
							  'unit': None,
							  'roles': [] }
				while True:
					first_name = input('Please enter resident first name: ')
					if first_name is not "": # ensure user inputs something
						break
				user_data['first_name'] = first_name
				while True:
					last_name = input('Please enter resident last name: ')
					if last_name is not "": # ensure user inputs something
						break
				user_data['last_name'] = last_name
				while True:
					unit = input('Please enter resident unit number: ')
					if unit is not "": # ensure user inputs something
						break
				user_data['unit'] = unit
				while True:
					role = input("Please enter all resident roles one at a time. Type 'stop' and hit enter to end: ")
					if role == 'stop':
						break
					elif role == "":
						# ignore null input
						continue
					else:
						user_data['roles'].append(role)
				data_source = move_in(user_data, data_source)
				try:
					write_data(data_source, 'property_data_changes.json')
				except:
					print('Error writing to file please check permissions and make sure it is not in use.')

			elif(user_input == 4): # Move out resident
				first_name = input('Please enter resident first name: ')
				last_name = input('Please enter resident last name: ')
				data_source = move_out(first_name, last_name, data_source)
				try:
					write_data(data_source, 'property_data_changes.json')
				except:
					print('Error writing to file please check permissions and make sure it is not in use.')

			elif(user_input == 5): # exit program
				break
	else:
		print('User not authorized. Exiting program...')

if __name__ == "__main__":
	main()