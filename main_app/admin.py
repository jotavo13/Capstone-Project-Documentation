from django.contrib import admin
from .models import Router, Switch, Documentation

# Register your models here.
admin.site.register(Router)
admin.site.register(Switch)
admin.site.register(Documentation)

