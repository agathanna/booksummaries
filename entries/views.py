from django.shortcuts import render
from .models import Book
from django.db.models import Q

def index(request): 
    entries = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(plot_summary__icontains=search))

        context = {
            'result': results
        }
        return render(request, 'entries/index.html', context)
    
    context = {'entries': entries}

    return render (request,  'entries/index.html', context ) 

def add(request):

    return render (request, 'entries/add.html' )

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'entries/upload.html')

def search(request):

    if request.method == 'GET':
        search= request.GET.get('search', '')
        post=Book.objects.all().filter(plot_summary="Search")

    return render (request, 'entries/search.html', {'post': post})



