import unittest
from check_functions import is_exit,is_empty
from file_system_calls import list_dbs

class TestUM(unittest.TestCase):
	
	def test1_is_exit(self):
		with self.assertRaises(SystemExit) as cm:
			is_exit('quit')
		self.assertEqual(cm.exception.code,1)

	def test1_is_empty(self):
		with self.assertRaises(SystemExit) as cm:
			is_empty([])
		self.assertEqual(cm.exception.code,1)

	def test2_is_empty(self):
		self.assertEqual(is_empty(['users.json']),None)

	def test1_list_dbs(self):
		self.assertEqual(list_dbs(),['organizations','tickets','users'])


if __name__ == '__main__':
    unittest.main()