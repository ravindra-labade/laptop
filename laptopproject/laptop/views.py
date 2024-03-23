from django.shortcuts import render, redirect
from .forms import LaptopForm
from .models import Laptop

def add_laptop(request):
    template_name = 'laptop/add.html'
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {"form": form}
    return render(request, template_name, context)


def show_laptop(request):
    template_name = 'laptop/show.html'
    laptops = Laptop.objects.all()
    context = {"laptops": laptops}
    return render(request, template_name, context)

def update_laptop(request, pk):
    template_name = 'laptop/add.html'
    obj = Laptop.objects.get(id=pk)
    form = LaptopForm(instance=obj)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        form.save()
        return redirect('show_url')
    context = {"form": form}
    return render(request, template_name, context)

def delete_laptop(request, pk):
    template_name = 'laptop/confirm.html'
    obj = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)