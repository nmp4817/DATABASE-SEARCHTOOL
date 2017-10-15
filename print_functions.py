import unicodedata

def print_dashline():
	print "\n"+"-"*100+"\n"

def print_keys(keys):
	print "\nSelect one of the following key to search:\n"

	for key in keys:
		print key

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

