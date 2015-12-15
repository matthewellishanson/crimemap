from django.shortcuts import render

from django.db.models import Count, Max, Avg

from .models import Incidentcode, Status, Building, Location, Incident

def homepage(request):
    incidents = Incident.objects.exclude(location__latitude=None).order_by('-reported')[:20]
    allincidents = Incident.objects.order_by('-reported')[:50]
    context = {"incidents": incidents, "allincidents": allincidents}
    return render(request, 'homepage.html', context)

def incidentdetail(request, case_no):
    incident = Incident.objects.get(casenumber=case_no)
    context = {"incident": incident}
    return render(request, 'incidentdetail.html', context)

def bigpicture(request):
    maxtheft = Incident.objects.order_by('-stolen').annotate(Max('stolen'))[:1]
    topcrime = Incidentcode.objects.annotate(num_incidentcodes=Count('incident')).order_by('-num_incidentcodes')[:5]
    topbuilding = Building.objects.annotate(num_buildings=Count('location__incident')).order_by('-num_buildings')[:5]
    context = {"maxtheft": maxtheft, "topcrime": topcrime, "topbuilding": topbuilding}
    return render(request, 'bigpicture.html', context)
    
    
    
