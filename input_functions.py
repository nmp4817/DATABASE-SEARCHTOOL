from check_functions import is_exit

def select_db(dbs):
	print "\nSelect one of the following database to search:\n"
		
	for db in dbs:
		print db+"\n"

	db_name = raw_input("\nPlease Enter the name of the database you want to search : ")
	db_name = db_name.lower().strip()

	is_exit(db_name)

	return db_name

def select_key():
	key_name = raw_input("\nPlease Enter the name of the key : ")
	key_name = key_name.lower().strip().replace(" ","")
	is_exit(key_name)
	return key_name

def enter_value(key_name):
	key_value = raw_input("\nPlease Enter value for the key "+key_name+" : ")
	key_value = key_value.lower().strip().replace(" ","")
	is_exit(key_value)
	return key_value