from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView

from .models import Transportation
from .forms import TransportForm



class IndexView(TemplateView):
    template_name = "transport/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        start_point = self.request.GET.get('start_point')
        end_point = self.request.GET.get('end_point')
        if start_point and end_point:
            buses = Transportation.objects.filter(Q(route__icontains=start_point) & Q(route__icontains=end_point))
            context['buses'] = buses
        return context


class About_us(TemplateView):
    template_name = "transport/about_us.html"

def transport_types(request):
    title = 'Types|Transportation'
    context = {'title':title}
    return render(request, 'transport/types.html', context)

def transport_list(request, t_type):
    title = 'All|Transports'
    transports = Transportation.objects.filter(type = t_type)
    context = {'title':title, 'transports':transports, 't_type':t_type}
    return render(request, 'transport/list_transport.html', context)
    

def transport_details(request, t_type, pk):
    transport = Transportation.objects.get(id = pk, type = t_type)
    title = f'N{transport.number}|{t_type.capitalize()}'
    context = {'title':title, 'transport':transport, 't_type':t_type}
    return render(request, 'transport/transport_details.html', context)


def create_transport(request):
    title = 'Create|Transport'
    form = TransportForm()
    if request.method == 'POST':
        form = TransportForm(request.POST) 
        if form.is_valid:
            form.save() 
            messages.success(request, 'The new transport was created!')
            return redirect('/')
        
    context = {'title':title, 'form' : form}
    return render(request, 'stop/create_stop.html', context)



def update_transport(request, pk):
    title = 'Update|Transport'
    transport = Transportation.objects.get(id=pk)
    form = TransportForm(instance = transport)
    
    if request.method == 'POST':
        form = TransportForm(request.POST, instance = transport)
        if form.is_valid:
            form.save()
            messages.success(request, 'The transport was updated successfully!')
            return redirect(transport)
    context = {'title':title, 'form' : form}
    return render(request, 'stop/create_stop.html', context)



def delete_transport(request, pk):
    title = 'Delete|Transport'
    transport = Transportation.objects.get(id = pk)
    
    if request.method == 'POST':
        transport.delete()
        return redirect('/')
    
    context = {'title':title, 'obj' : transport}
    return render(request, 'delete.html', context)