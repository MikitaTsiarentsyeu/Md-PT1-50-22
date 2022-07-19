from django.shortcuts import redirect, render
from .models import Row
from .forms import AddRow
from datetime import datetime


# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):

    rows = Row.objects.all()

    return render(request, 'dashboard.html', {'rows':rows})

def add_row(request):
    if request.method == "POST":
        form = AddRow(request.POST)

        if form.is_valid():
            row = form.save(commit=False)
            row.date = datetime.now()

            row.save()
            form.save_m2m

        return redirect ('dashboard')
    else:
        form = AddRow()

    return render (request, 'add_row.html', {'form':form})