from django.shortcuts import render, get_object_or_404

from .models import Shoe, Run

def dashboard(request):
    return render(request, 'runlog/base.html', {})

def shoes(request):
    shoes = Shoe.objects.all()
    return render(request, 'runlog/shoes.html', {'shoes':shoes})

def add_shoe(request):
    return render(request, 'runlog/base.html', {})