from django.conf.urls import url
from django.views.generic import TemplateView
#from django.views.generic.edit import ProcessFormView
from . import views

urlpatterns = [

    url(r'^search', TemplateView.as_view(template_name= "bot/index.html"), name="bot"),
    ]