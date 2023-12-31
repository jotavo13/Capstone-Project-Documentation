from django.db import models

# Create your models here.
class Router(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title", default='', blank=True)
    model = models.CharField(max_length=100, verbose_name="Model", default='', blank=True)
    information = models.TextField(verbose_name="Information", default='', blank=True)
    img = models.CharField(max_length=250, verbose_name="Image", default='', blank=True)



    def __str__(self):
        return self.title
    
class Switch(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title", default='', blank=True)
    model = models.CharField(max_length=100, verbose_name="Model", default='', blank=True)
    information = models.TextField(verbose_name="Information", default='', blank=True)
    img = models.CharField(max_length=250, verbose_name="Image", default=' ', blank=True)



    def __str__(self):
        return self.title
    


class Documentation(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    scheduling = models.TextField(max_length=100, verbose_name="Scheduling")
    information = models.TextField(verbose_name="Information")
    vendorContact = models.TextField(verbose_name="VendorContact")
    img = models.CharField(max_length=250, verbose_name="Image", default=' ', blank=True)



    def __str__(self):
        return self.title