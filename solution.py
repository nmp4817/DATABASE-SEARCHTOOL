import sys
import os
import json
import unicodedata


def print_dashline():
	print "\n"+"-"*100+"\n"

def is_exit(user_input):
	if user_input == 'quit':
		print_dashline()
		print ("\t\t\t\t\t THANKS FOR BROWSING OUR DATABASE!")
		print_dashline()
		os._exit(1)

def is_empty(l):
	if len(l) == 0:
		print "\n Database is empty!"
		is_exit("quit")


def list_dbs():
	dbs = []

	for file in os.listdir("."):
	    if file.endswith(".json"):
     		name,ext = file.split(".")
     		dbs.append(name)

	return dbs

def select_db(dbs):
	print "\nSelect one of the following database to search:\n"
		
	for db in dbs:
		print db+"\n"

	db_name = raw_input("\nPlease Enter the name of the database you want to search : ")
	db_name = db_name.lower().strip()

	is_exit(db_name)

	return db_name


def read_db(db_name):
	with open(db_name+".json") as json_f:
		json_data = json.load(json_f)
		return json_data

def print_keys(keys):
	print "\nSelect one of the following key to search:\n"

	for key in keys:
		print key

def select_key():
	key_name = raw_input("\nPlease Enter the name of the key : ")
	key_name = key_name.lower().strip().replace(" ","")
	is_exit(key_name)
	return key_name

def enter_value():
	key_value = raw_input("\nPlease Enter value for the key "+key_name+" : ")
	key_value = key_value.lower().strip().replace(" ","")
	is_exit(key_value)
	return key_value

def search(key_name,key_value,json_data):
	matching_objects = []

	for json_object in json_data:
		if key_name in json_object:
			if isinstance(json_object[key_name],list):
				for v in json_object[key_name]:
					if isinstance(v,unicode):
						if str(v.encode("ascii","ignore")).strip().lower().replace(" ","") ==  str(key_value):
							matching_objects.append(json_object)
							break
					else:
						if str(json_object[key_name]).strip().lower().replace(" ","") ==  str(key_value):
							matching_objects.append(json_object)
							break
			else:
				if isinstance(json_object[key_name],unicode):
					if str(json_object[key_name].encode("ascii","ignore")).strip().lower().replace(" ","") ==  str(key_value):
						matching_objects.append(json_object)
				else:
					if str(json_object[key_name]).strip().lower().replace(" ","") ==  str(key_value):
						matching_objects.append(json_object)

	return matching_objects


def print_output(matching_objects):
	print_dashline()
	print "\t\t\t\t\tOUTPUT : "
	print_dashline()

	if len(matching_objects) > 0 :
		for obj in matching_objects:
			for k in obj:
				if isinstance(obj[k],list):
					l = []
					for v in obj[k]:
						if isinstance(v,unicode):
							l.append(unicodedata.normalize('NFKD', v).encode('ascii','ignore'))
						else:
							l.append(obj[k])
					print "\n" + k + " : " + str(l)

				elif isinstance(obj[k],unicode):
					print "\n" + k + " : " + unicodedata.normalize('NFKD', obj[k]).encode('ascii','ignore')

				else:
					print "\n" + k + " : " + str(obj[k])

			print_dashline()
	else:
		print "\t\t\tRecord does not exist!"

	print_dashline()


if __name__ == "__main__":
	print "\nWelcome to Zendesk database search: "

	print "\n\tType quit to exit anytime!"

	dbs = list_dbs()

	is_empty(dbs)

	while(1):

		db_name = select_db(dbs)

		if db_name in dbs:                                                   
			json_data = read_db(db_name)

			keys = json_data[0].keys()

			while(1):

				print "\n\tType quit to exit anytime!  Type previous to select different databse!\n"

				print_keys(keys)

				key_name = select_key()

				if key_name == "previous":
					break

				if key_name in keys:
					key_value = enter_value()

					if key_value == "previous":
						break
					
					if not key_value.isalnum():
						key_value = key_value.decode('ascii','ignore')

					matching_objects = search(key_name,key_value,json_data)

					print_output(matching_objects)
					
				else:
					print "\n\tError : Please select from given choices !!!\n"
		else:
			print "\n\tError : Please select from given choices !!!\n"
	
