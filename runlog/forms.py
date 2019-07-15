from django.forms import ModelForm

from .models import Run, Shoe

class ShoeForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'brand', 'model', 'date_purchased', 'starting_mileage']

class RunForm(ModelForm):
    class Meta:
        model = Run
        fields = ['distance', 'time', 'notes', 'race', 'datetime'] 