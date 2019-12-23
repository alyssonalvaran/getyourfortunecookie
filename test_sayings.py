from sayings import get_sayings_list, get_random_saying, overwrite_saying


class TestClass:
	def test_get_sayings_list(self):
		"""
		Test if get_sayings_list returns a list of strings
		"""
		file_path = "static/temp/cookie-sayings.txt"
		sayings_list = get_sayings_list(file_path)

		assert type(sayings_list) == list and type(sayings_list[0]) == str

	def test_get_random_saying(self):
		"""
		Test if get_random_saying return a string saying and an integer index
		"""
		file_path = "static/temp/cookie-sayings.txt"
		saying, index = get_random_saying(file_path)

		assert type(saying) == str and type(index) == int

	def test_overwrite_saying(self):
		"""
		Test if overwrite_saying overwrites the previous value of the file
		"""
		file_path = "static/temp/test-cookie-sayings.txt"
		saying, index = get_random_saying(file_path)
		overwrite_saying(file_path, index, saying)

		sayings_list = get_sayings_list(file_path)

		assert sayings_list[index] == saying