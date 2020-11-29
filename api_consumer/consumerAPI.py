from urllib.request import urlopen
import json

def datareceived1():
	url = 'https://jsonplaceholder.typicode.com/todos/1'
	data = urlopen(url)
	person = json.load(data)

	return person
	
def datareceived2():
	url = 'https://jsonplaceholder.typicode.com/todos/1'
	data = urlopen(url)
	result = json.load(data)

	return result 

def SpaceXLaunchesPast():
	url = 'https://api.spacexdata.com/v2/launches'
	data = urlopen(url)
	result = json.load(data)

	return result


AllDataLaunches = SpaceXLaunchesPast()

for i in AllDataLaunches:
	print(i['mission_name'])
	print(', ')
	print(i['launch_year'])

