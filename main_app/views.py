from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django import forms


from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# importing models
from .models import Router, Switch, Documentation



# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
############ROUTERS############
############ROUTERS############
############ROUTERS############
    
class RouterList(TemplateView):
    template_name = 'router_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # the characters object will also give you access to the character class model that's related to it
        context['routers'] = Router.objects.all()
        return context
    


class RouterCreate(CreateView):
    model = Router
    # these fields are what the user sees/can input when creating a new character
    fields = ['title', 'img', 'model', 'information', 'configuration']
    template_name = 'router_create.html'
    success_url = '/routers/'



############SWITCH############
############SWITCH############
############SWITCH############

    
class SwitchList(TemplateView):
    template_name = 'switch_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # the characters object will also give you access to the character class model that's related to it
        context['switchs'] = Switch.objects.all()
        return context
    


class SwitchCreate(CreateView):
    model = Switch
    # these fields are what the user sees/can input when creating a new character
    fields = ['title', 'img', 'model', 'information', 'configuration']
    template_name = 'switch_create.html'
    success_url = '/switchs/'


############DOCUMETATION############
############DOCUMETATION############
############DOCUMETATION############

    
    
class DocumentationList(TemplateView):
    template_name = 'documentation_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # the characters object will also give you access to the character class model that's related to it
        context['documentations'] = Documentation.objects.all()
        return context
    


class DocumentationCreate(CreateView):
    model = Documentation
    # these fields are what the user sees/can input when creating a new character
    fields = ['title', 'img', 'scheduling', 'information', 'vendorContact']
    template_name = 'documentation_create.html'
    success_url = '/documentations/'


