from django.shortcuts import render

def listfun(request):
    context= {
         'list1':['cse','ise','ec','mec','aiml','civil'],
        'list2':['fsd','st','vlsi','os','ai','ope']
    }
    return render(request,"displaylist.html",context)
# Create your views here.
