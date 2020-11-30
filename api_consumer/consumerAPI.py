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

def SettingDateLaunches(AllDataLaunches):
	val = 'hola'
	myDict = {}
	mylist = [50]

	j = 0

	for i in AllDataLaunches:


		myDict['mission_name'] = i['mission_name']
		myDict['launch_year' ] = i['launch_year']
		myDict['launch_success'] = i['launch_success']
		myDict['upcoming'] = i['upcoming']
		myDict['launch_site'] = i['launch_site']['site_name']
		myDict['rocket_name'] = i['rocket']['rocket_name']
		myDict['yt_video_link'] = i['links']['video_link']

		mylist[0] = myDict	

		return mylist


result = SettingDateLaunches(AllDataLaunches)
print(result)

