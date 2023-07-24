from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django import forms


from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# importing models
from .models import Router, Switch, Documetation

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class RoutertList(TemplateView):
    template_name = 'router_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # the characters object will also give you access to the character class model that's related to it
        context['routers'] = Router.objects.all()
        return context
    

class RouterForm(forms.ModelForm):
    class Meta:
        model = Router
        fields = ['title', 'img', 'information', 'configuration']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


