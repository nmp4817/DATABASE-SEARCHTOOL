import unicodedata

def search(key_name,key_value,json_data):
	matching_objects = []

	for json_object in json_data:
		if key_name in json_object:
			match = search_object(key_name, key_value, json_object)
			if match == True: matching_objects.append(json_object)

	return matching_objects

def search_object(key_name,key_value,json_object):
	if isinstance(json_object[key_name],list):
		for v in json_object[key_name]:
			if isinstance(v,unicode):
				if str(v.encode("ascii","ignore")).strip().lower().replace(" ","") ==  str(key_value):
					return True
			else:
				if str(json_object[key_name]).strip().lower().replace(" ","") ==  str(key_value):
					return True
	else:
		if isinstance(json_object[key_name],unicode):
			if str(json_object[key_name].encode("ascii","ignore")).strip().lower().replace(" ","") ==  str(key_value):
				return True
		else:
			if str(json_object[key_name]).strip().lower().replace(" ","") ==  str(key_value):
				return True
	return False
