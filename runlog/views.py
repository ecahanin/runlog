from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Shoe, Run
from .forms import ShoeForm


@login_required(login_url='/login/')
def dashboard(request):
    user = request.user
    return render(request, 'runlog/base.html', {})

@login_required(login_url='/login/')
def shoes(request):
    user = request.user
    shoes = Shoe.objects.filter(owner=user.id)
    return render(request, 'runlog/shoes.html', {'shoes':shoes, 'user':user})

@login_required(login_url='/login/')
def add_shoe(request):
    shoeform = ShoeForm()
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            shoe = form.save(commit=False)
            shoe.owner = request.user
            shoe.save()
            return HttpResponseRedirect(shoe.get_absolute_url())
    return render(request, 'runlog/new_shoe.html', {'form':shoeform})

@login_required(login_url='/login/')
def shoe_details(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    return render(request, 'runlog/shoe_details.html', {'shoe':shoe})

