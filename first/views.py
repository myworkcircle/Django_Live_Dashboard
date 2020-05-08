from django.http import HttpResponse
from django.shortcuts import render
from .forms import calculation,Hospital_Info
from .models import Hospital,Rooms

""" Index """
def Home_Page(request):
    hos = Hospital.objects.all()
    return render(request,'dashboard/statistics.html',{'ho':hos})

""" rooms data """
def Data_Input(request):
    form = calculation(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,'forms/Data_Input.html',context)

""" Hospital data"""
def Hospital_Data_View(request):
    form = Hospital_Info(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,'forms/Hospital_Data.html',context)



