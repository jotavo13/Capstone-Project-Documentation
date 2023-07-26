from django.shortcuts import render, redirect
import json
from django.http import HttpResponse


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

class RouterDetail(DetailView):
    model = Router
    template_name = 'router_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class RouterUpdate(UpdateView):
    model = Router
    fields = ['title', 'img', 'model', 'information', 'configuration']
    template_name = 'router_update.html'
    success_url = '/routers/'

class RouterDelete(DeleteView):
    model = Router
    template_name = 'router_delete_confirmation.html'

    success_url = '/routers/'

############SWITCH############
############SWITCH############
############SWITCH############

    
class SwitchList(TemplateView):
    template_name = 'switch_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # the characters object will also give you access to the character class model that's related to it
        context['switches'] = Switch.objects.all()
        return context
    


class SwitchCreate(CreateView):
    model = Switch
    # these fields are what the user sees/can input when creating a new character
    fields = ['title', 'img', 'model', 'information', 'configuration']
    template_name = 'switch_create.html'
    success_url = '/switches/'


class SwitchDetail(DetailView):
    model = Switch
    template_name = 'switch_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SwitchUpdate(UpdateView):
    model = Switch
    fields = ['title', 'img', 'model', 'information', 'configuration']
    template_name = 'switch_update.html'
    success_url = '/switches/'

class SwitchDelete(DeleteView):
    model = Switch
    template_name = 'switch_delete_confirmation.html'

    success_url = '/switches/'


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


class DocumentationDetail(DetailView):
    model = Documentation
    template_name = 'documentation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class DocumentationUpdate(UpdateView):
    model = Documentation
    fields = ['title', 'img', 'scheduling', 'information', 'vendorContact']
    template_name = 'documentation_update.html'
    success_url = '/documentations/'

class DocumentationDelete(DeleteView):
    model = Documentation
    template_name = 'documentation_delete_confirmation.html'

    success_url = '/documentations/'

