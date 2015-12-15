import os, sys, string, csv, datetime, time, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crime.settings")

from django.conf import settings

django.setup()

from crimemap.models import Incidentcode, Status, Building, Location, Incident

from django.template.defaultfilters import slugify, urlize

reader = csv.reader(open("crimelog.csv", "rU"), dialect=csv.excel)
reader.next()

for row in reader:
    #try:
        incuni = unicode(row[1], errors='ignore')
        inc, inccreated = Incidentcode.objects.get_or_create(name=incuni, name_slug=slugify(incuni))
        statuni = unicode(row[3], errors='ignore')
        stat, statcreated = Status.objects.get_or_create(name=statuni, name_slug=slugify(statuni))
        if row[6] == "":
            build = None
        else: 
            builduni = unicode(row[6], errors='ignore')
            build, buildcreated = Building.objects.get_or_create(name=builduni, name_slug=slugify(builduni))    
        locuni = unicode(row[7], errors='ignore')
        locsplit = locuni.split('(')
        loc, loccreated = Location.objects.get_or_create(name=locsplit[0], name_slug=slugify(locsplit[0]), building=build)
        if row[8] != "":
            try: 
                stln = float(row[8].replace('$', '').replace(',',''))
            except:
                stln = ""
        else:
            stln = ""
        if row[9] != "":
            try:
                dmg = float(row[9].replace('$', '').replace(',',''))
            except:
                dmg = ""
        else:
            dmg = ""
        if row[2] != "":
            reportdate = time.strptime(row[2], "%m/%d/%Y %H:%M")
            reportdate = datetime.datetime(reportdate.tm_year, reportdate.tm_mon, reportdate.tm_mday, reportdate.tm_hour, reportdate.tm_min)
        else:
            reportdate = None
        if row[4] != "":
            startdate = time.strptime(row[4], "%m/%d/%Y %H:%M")
            startdate = datetime.datetime(startdate.tm_year, startdate.tm_mon, startdate.tm_mday, startdate.tm_hour, startdate.tm_min)
        else:
            startdate = None
        if row[5] != "":
            enddate = time.strptime(row[5], "%m/%d/%Y %H:%M")
            enddate = datetime.datetime(enddate.tm_year, enddate.tm_mon, enddate.tm_mday, enddate.tm_hour, enddate.tm_min)
        else:
            enddate = None
        incid, incidcreated = Incident.objects.get_or_create(casenumber=row[0], incidentcode=inc, reported=reportdate, status=stat, start=startdate, end=enddate, location=loc, stolen=stln, damaged=dmg, description=row[10])
    #except:
    #    print row[0]
    
    

    

        
        

    



        

    



