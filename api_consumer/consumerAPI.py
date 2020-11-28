from urllib.request import urlopen
import json

def datareceived1():
	url = 'some url'
	data = urlopen(url).read()
	person = json.load(data)

	return person
	
def datareceived2():