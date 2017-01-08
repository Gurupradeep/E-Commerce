from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BotForm
import time
from bot.files import *
# Create your views here.

def process(request):
	results=[]
	if request.method == 'POST':
		myform = BotForm(request.POST)
		if myform.is_valid():
			text=myform.cleaned_data['search_text']
			print(text)
			crawler_machine(text)
			time.sleep(100)
			results=fetch_by_title(text)
			#print(result)
			#print("hi")
		#print("hello")
	return render(request,"bot/results.html",{'results':results})