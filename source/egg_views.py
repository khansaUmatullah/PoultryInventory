from django.shortcuts import render, get_object_or_404, redirect
from .models import Egg, Chicken
from .forms import EggForm

# List all eggs
def egg_list(request):
    eggs = Egg.objects.all()
    return render(request, 'egg_list.html', {'eggs': eggs})

def add_eggs(request, chicken_id):
    chicken = get_object_or_404(Chicken, pk=chicken_id)
    if request.method == 'POST':
        form = EggForm(request.POST)
        if form.is_valid():
            egg = form.save(commit=False)
            egg.chicken = chicken
            egg.save()
            return redirect('egg_list')
    else:
        form = EggForm()
    return render(request, 'add_eggs.html', {'form': form, 'chicken': chicken})
