from django.conf.urls import url
from django.views.generic import TemplateView
#from django.views.generic.edit import ProcessFormView
from . import views

urlpatterns = [
	url(r'^process/',views.process,name="process"),
    url(r'^search', TemplateView.as_view(template_name= "bot/main.html"), name="bot"),
    url(r'^results', TemplateView.as_view(template_name= "bot/results.html"), name="bot"),
    url(r'^index', TemplateView.as_view(template_name= "bot/index.html"), name="bot"),
    url(r'^new_base', TemplateView.as_view(template_name= "bot/new_base.html"), name="bot"),

    ]