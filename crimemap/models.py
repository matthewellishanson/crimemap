from django.db import models

class Incidentcode(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/inccode/%i/" % self.id

class Status(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name
    
class Building(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=150)
    name_slug = models.SlugField()
    building = models.ForeignKey(Building, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Incident(models.Model):
    casenumber = models.CharField(max_length=10)
    incidentcode = models.ForeignKey(Incidentcode)
    reported = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Status)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    location = models.ForeignKey(Location)
    stolen = models.FloatField(blank=True, null=True)
    damaged = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return self.casenumber
    def get_absolute_url(self):
        return "incidents/%s" % self.casenumber

