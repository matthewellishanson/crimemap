import os, sys, string, csv, datetime, time, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crime.settings")

from django.conf import settings

from crimemap.models import Incidentcode, Status, Building, Location, Incident

from django.template.defaultfilters import slugify, urlize

reader = csv.reader(open("crimelog.csv", "rU"), dialect=csv.excel)
reader.next()

for row in reader:
    inc, inccreated = Incidentcode.objects.get_or_create(name=row[1], name_slug=slugify(row[1]))
    print inc
        
        

    



