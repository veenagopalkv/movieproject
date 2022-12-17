from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import movie

# Create your views here.
def index(request):
    movien=movie.objects.all()
    context={
        'movie_list':movien
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movies = movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movies})

def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        year=request.POST.get('year')
        image=request.FILES['image']
        movies1=movie(name=name,description=description,year=year,image=image)
        print(movies1)
        movies1.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movieval=movie.objects.get(id=id)
    forms=MovieForm(request.POST or None,request.FILES,instance=movieval)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':forms,'movie':movieval})

def delete(request,id):
    if request.method == 'POST':
        movievall=movie.objects.get(id=id)
        movievall.delete()
        return redirect('/')
    return render(request,'delete.html')
