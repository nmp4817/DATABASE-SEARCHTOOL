from file_system_calls import list_dbs,read_db
from print_functions import print_keys,print_output
from check_functions import is_exit,is_empty
from input_functions import select_db,select_key,enter_value
from search_functions import search

if __name__ == "__main__":
	try:
		print "\nWelcome to Zendesk database search: "

		print "\n\tType quit to exit anytime!"

		dbs = list_dbs()

		is_empty(dbs)

		json_data = {}

		while(1):

			db_name = select_db(dbs)

			if db_name in dbs: 
				if db_name not in json_data:
					json_data[db_name] = read_db(db_name)

				keys = json_data[db_name][0].keys()	

				while(1):

					print "\n\tType quit to exit anytime!  Type previous to select different databse!\n"

					print_keys(keys)

					key_name = select_key()

					if key_name == "previous":
						break

					if key_name in keys:
						key_value = enter_value(key_name)

						if key_value == "previous":
							break
						
						if not key_value.isalnum():
							key_value = key_value.decode('ascii','ignore')

						matching_objects = search(key_name,key_value,json_data[db_name])

						print_output(matching_objects)
						
					else:
						print "\n\tError : Please select from given choices !!!\n"
			else:
				print "\n\tError : Please select from given choices !!!\n"

	except Exception,e:
		print "\n\n System Error! Please Try again after some time! \n\n"
		is_exit('quit')
