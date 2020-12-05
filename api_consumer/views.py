from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .consumerAPI import SpaceXLaunchesPast
from .models import LaunchesSpaceX, ClassName

def name(req):
	nombre = 'Silvio'

	myname = ClassName(name = nombre)
	myname.save()

	alls = ClassName.objects.all()
	context = {'name':alls}
	return render(req,'name.html',context)


def seeing_space_data(req):
	#esto solo serviria the first time cause the db later alreadey would have the data in itself
	AllDataLaunches = SpaceXLaunchesPast()
	j = 0
	mylist = []

	for i in AllDataLaunches:
		ready = LaunchesSpaceX(mission_name = i['mission_name'] )
		ready.save()
		print(j) 
		j += 1

	context = { 'name' : AllDataLaunches}

	return render(req,'spaceX.html', context )

def init_view(req):
	return render(req,'init_.html')