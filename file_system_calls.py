import os
import json

def list_dbs():
	dbs = []

	for file in os.listdir("."):
	    if file.endswith(".json"):
     		name,ext = file.split(".")
     		dbs.append(name)

	return dbs

def read_db(db_name):
	with open(db_name+".json") as json_f:
		json_data = json.load(json_f)
		return json_data