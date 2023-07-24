from django.db import models

# Create your models here.
class Router(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    model = models.CharField(max_length=100, verbose_name="Model")
    information = models.CharField(verbose_name="Information")
    configuration = models.CharField(verbose_name="Configuration")
    img = models.CharField(max_length=250, verbose_name="Image", default=' ', blank=True)



    def __str__(self):
        return self.title
    
class Switch(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    model = models.CharField(max_length=100, verbose_name="Model")
    information = models.CharField(verbose_name="Information")
    configuration = models.CharField(verbose_name="Configuration")
    img = models.CharField(max_length=250, verbose_name="Image", default=' ', blank=True)



    def __str__(self):
        return self.title
    


class Documetation(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    scheduling = models.CharField(max_length=100, verbose_name="Scheduling")
    information = models.CharField(verbose_name="Information")
    vendorContact = models.CharField(verbose_name="VendorContact")
    img = models.CharField(max_length=250, verbose_name="Image", default=' ', blank=True)



    def __str__(self):
        return self.title