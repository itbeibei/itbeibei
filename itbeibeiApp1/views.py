from django.shortcuts import render
from models import *
# Create your views here.



def home(request):
    testname = test.objects.all()
    return render(request,'home.html',locals())