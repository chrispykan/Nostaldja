from django.shortcuts import render, redirect
from .models import Decade, Fad

# Create your views here.

# Decade  Index
def decade_list(request):
    decades = Decade.objects.all().order_by('start_year')
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})


# Decade Show/Read
def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})

# Decade New/Create
def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})

# Decade Edit/Update
def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_form.html', {'form': form})

# Decade Delete/Destroy
def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')



# Fad  Index
def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})

# Fad Show/Read
def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})

# Fad New/Create
def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        print(form)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
        decades = Decade.objects.all()
    return render(request, 'nostaldja/fad_form.html', {'form': form})

# Fad Edit/Update
def fad_edit(request, pk):
    fad = Fad.objects.get(pk=pk)
    if request.method == "POST":
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja/fad_form.html', {'form': form})

# Fad Delete/Destroy
def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
