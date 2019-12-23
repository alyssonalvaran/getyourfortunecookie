from random import randrange


def get_sayings_list(file_path):
	f = open(file_path, "r")
	sayings = f.read()
	sayings_list = sayings.split("\n")
	f.close()

	return sayings_list

def get_random_saying(file_path):
	sayings_list = get_sayings_list(file_path)

	index = randrange(len(sayings_list))
	saying = sayings_list[index]

	return saying, index

def overwrite_saying(file_path, index, saying_input):
	sayings_list = get_sayings_list(file_path)

	if saying_input != "":
		sayings_list[index] = saying_input
		
		f = open(file_path, "w")
		f.write("\n".join(sayings_list))
		f.close()