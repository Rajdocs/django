from django.shortcuts import render
from datetime import datetime,timedelta

def datetime_offset(request):
    now=datetime.now()
    context={
        "current_time":now,
        "fourhour_ahead":now+timedelta(hours=4),
        "fourhour_before":now-timedelta(hours=4),
    }
    return render(request,"offsettime.html",context)

# Create your views here.
