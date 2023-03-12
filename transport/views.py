from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from helpers.decorators_own import action_superuser

from .forms import TransportForm
from .models import Transportation


class IndexView(TemplateView):
    """ View for the Home page and for handling the search of transportations based on the route input """

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


def transport_types(request):
    """ View for transportation types """

    title = 'Types|Transportation'
    context = {'title': title}
    return render(request, 'transport/types.html', context)


def transport_list(request, t_type):
    """ View to handle all the specified transportation types """

    title = 'All|Transports'
    transports = Transportation.objects.filter(type=t_type)
    context = {'title': title, 'transports': transports, 't_type': t_type}
    return render(request, 'transport/list_transport.html', context)


def transport_details(request, t_type, pk):
    """ View for showing the average rating and route for each bus """

    transport = Transportation.objects.get(pk=pk, type=t_type)
    title = f'N{transport.number}|{t_type.capitalize()}'
    avg_rate = transport.average_rating()
    routes = transport.route.split("-")
    context = {'title': title, 'transport': transport, 't_type': t_type, 'avg_rate': avg_rate, 'routes': routes}
    print(routes)
    return render(request, 'transport/transport_details.html', context)


@action_superuser
def create_transport(request):
    """ Creates transportation """

    title = 'Create|Transport'
    form = TransportForm()
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'The new transport was created!')
            return redirect('/')

    context = {'title': title, 'form': form}
    return render(request, 'stop/create_stop.html', context)


@action_superuser
def update_transport(request, pk):
    """ Updates transportation """

    title = 'Update|Transport'
    transport = get_object_or_404(Transportation, pk=pk)
    form = TransportForm(instance=transport)

    if request.method == 'POST':
        form = TransportForm(request.POST, instance=transport)
        if form.is_valid:
            form.save()
            messages.success(request, 'The transport was updated successfully!')
            return redirect(transport)
    context = {'title': title, 'form': form}
    return render(request, 'stop/create_stop.html', context)


@action_superuser
def delete_transport(request, pk):
    """ Deletes transportation """

    title = 'Delete|Transport'
    transport = Transportation.objects.get(id=pk)

    if request.method == 'POST':
        transport.delete()
        return redirect('/')

    context = {'title': title, 'obj': transport}
    return render(request, 'delete.html', context)
