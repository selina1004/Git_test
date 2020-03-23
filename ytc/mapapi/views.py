from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Place_info
from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm

def place_list(request):
    posts = Place_info.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'mapapi/place_list.html', {'posts': posts})

def place_new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            place_info = form.save(commit=False)
            place_info.created_date = timezone.now()
            place_info.save()
            return redirect('place_new', pk=place_info.pk)
    else:
        form = RegisterForm()
    return render(request, 'mapapi/place_new.html', {'form': form})