from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .consumerAPI import datareceived1, datareceived2
from .models import theModel

def saving(req):
	data1 = datareceived1
	data2 = datareceived2

	data1over = theModel(first_field = data1.someFieldJsonDependOfthepage)
	data1over = theModel(other_field = data1.otherFieldfromthepage)
	data1over.save()

	# and thus i can fill the fields 

	return HttpResponseRedirect('/input_data/')

