# Writes new data to file
def write_data(data):
	with open('data/stats.txt', 'a') as data_file:
		exercise = data['exercise']
		count = data['count']
		data_file.write('{}:{}\n'.format(exercise, count))

# Reads data, returns as dictionary
def read_data():
	with open('data/stats.txt', 'r') as data_file:
		data = {}
		for line in data_file:
			line = line.strip()
			exercise, count = line.split(':')
			if exercise in data.keys():
				data[exercise].append(count)
			else:
				data[exercise] = []
				data[exercise].append(count)
	return data

# Clears data, for debugging purposes
def clear_data():
	with open('data/stats.txt', 'w') as data_file:
		data_file.write('')