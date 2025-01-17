from django.shortcuts import render, get_object_or_404, redirect
from .models import Chicken
from .forms import ChickenForm

def chicken_list(request):
    chickens = Chicken.objects.all()
    return render(request, 'chicken_list.html', {'chickens': chickens})

def add_chicken(request):
    if request.method == 'POST':
        form = ChickenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chicken_list')
    else:
        form = ChickenForm()
    return render(request, 'add_chicken.html', {'form': form})

def edit_chicken(request, pk):
    chicken = get_object_or_404(Chicken, pk=pk)
    if request.method == 'POST':
        form = ChickenForm(request.POST, instance=chicken)
        if form.is_valid():
            form.save()
            return redirect('chicken_list')
    else:
        form = ChickenForm(instance=chicken)
    return render(request, 'edit_chicken.html', {'form': form})

def delete_chicken(request, pk):
    chicken = get_object_or_404(Chicken, pk=pk)
    if request.method == 'POST':
        chicken.delete()
        return redirect('chicken_list')
    return render(request, 'delete_chicken.html', {'chicken': chicken})
