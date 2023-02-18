from django.forms import ModelForm
from .models import BusStop

class StopForm(ModelForm):
    
    class Meta:
        model = BusStop
        fields = '__all__'
        

