from urllib.request import urlopen
import json

def SpaceXLaunchesPast():
	url = 'https://api.spacexdata.com/v2/launches'
	data = urlopen(url)
	result = json.load(data)

	return result



		



