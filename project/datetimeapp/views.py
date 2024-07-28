from django.shortcuts import render
from datetime import datetime

def date_time(request):
    now=datetime.now()
    context={"datetimeview":now}
    return render(request,"datetimetemplate.html",context)

# Create your views here.
