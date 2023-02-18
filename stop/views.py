from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BusStop
from .forms import StopForm

# Create your views here.
def regions(request):
    title = 'Regions|Stops'
    stops = BusStop.objects.all()
    regions = []
    
    for stop in stops:
        if stop.region.capitalize() not in regions:
            regions.append(stop.region.capitalize())
        
    
    context = {'title':title, 'regions':regions}
    return render(request, 'stop/regions.html', context)


def region_stops(request, region):
    title = f'Stops|{region}'
    stops = BusStop.objects.filter(region = region.lower())
    context = {'title':title, 'region':region, 'stops':stops}
    return render(request, 'stop/region_stops.html', context)
    

def stop_details(request, pk):
    stop = BusStop.objects.get(id = pk)
    title = f'{stop.letter}|Stop'
    context = {'title':title, 'stop':stop}
    return render(request, 'stop/stop_details.html', context)


def create_stop(request):
    title = 'Create|Stop'
    form = StopForm()
    print(11)
    if request.method == 'POST':
        print(22)
        form = StopForm(request.POST) 
        if form.is_valid:
            print(33)
            form.save() 
            messages.success(request, 'The new stop was created!')
            return redirect('/')
        
    print(44)
    context = {'title':title, 'form' : form}
    return render(request, 'stop/create_stop.html', context)



def update_stop(request, pk):
    title = 'Update|Stop'
    stop = BusStop.objects.get(id=pk)
    form = StopForm(instance = stop)
    
    if request.method == 'POST':
        form = StopForm(request.POST, instance = stop)
        if form.is_valid:
            form.save()
            messages.success(request, 'The stop was updated successfully!')
            return redirect(stop)
    context = {'title':title, 'form' : form}
    return render(request, 'stop/create_stop.html', context)



def delete_stop(request, pk):
    title = 'Delete|Stop'
    stop = BusStop.objects.get(id = pk)
    
    if request.method == 'POST':
        stop.delete()
        return redirect('/')
    
    context = {'title':title, 'obj' : stop}
    return render(request, 'delete.html', context)


    