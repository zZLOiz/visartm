from django.shortcuts import render, redirect
from django.template import RequestContext, Context, loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
 
def start_page(request):
    return render(request, 'index.html', Context({'no_footer' : True}))

def settings_page(request):
	template = loader.get_template('settings.html')
	themes = ["dark", "light"]
	context = Context({'themes': themes, 
						'user':request.user})
	return render(request, 'settings.html', context)  
	
def	help_page(request):
	return render(request, 'help.html')
	
def message(request, message):
	return render(request, 'message.html', Context({'message': message}))

def wait(request, message, begin, period = "5"):
	message = "<meta http-equiv='refresh' content='" + period + "'>" + message + \
		"<br>Elapsed: " + str((datetime.now() - begin).seconds) + " sec."
	return HttpResponse(message)
	