import imp
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime
def home(request):
    print(request)
    return render(request, 'home/welcome.html',{'today': datetime.today()})