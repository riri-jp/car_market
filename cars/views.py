from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


def car_list(request):
    cars = Car.objects.all()
    context = {
        "cars": cars,
    }
    return render(request, 'car_list.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
        "car": car,
    }
    return render(request, 'car_detail.html', context)


def car_create(request):
    form = CarForm()
    
    if request.method == "POST":

        form = CarForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'NICEEEE')
            return redirect('car-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)



def car_update(request, car_id):
    car = Car.objects.get(id=car_id)
    form = CarForm(instance = car)
    if request.method == "POST":

        form = CarForm(request.POST, request.FILES or None, instance = car)
        if form.is_valid():
            form.save()
            messages.info(request, 'what!! why?')
            return redirect('car-detail', car_id=car_id )
    context = {
        "form": form,
        "car": car,
    }
    return render(request, 'update.html', context)
    

def car_delete(request, car_id):
    Car.objects.get(id=car_id).delete()
    messages.warning(request, 'You suck')
    return redirect('car-list')
    