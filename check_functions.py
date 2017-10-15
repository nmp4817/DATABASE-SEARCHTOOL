import sys
from print_functions import print_dashline

def is_exit(user_input):
	if user_input == 'quit':
		print_dashline()
		print ("\t\t\t\t\t THANKS FOR BROWSING OUR DATABASE!")
		print_dashline()
		sys.exit(1)

def is_empty(l):
	if len(l) == 0:
		print "\n Database is empty!"
		is_exit("quit")