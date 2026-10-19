from django.shortcuts import render, redirect
from .forms import CarForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('success')

    else:
        form = CarForm()

    return render(
        request,
        'core/home.html',
        {'form': form})


def success(request):
    return render(request, 'core/success.html')