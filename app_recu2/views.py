from django.http import request
from django.http import HttpResponse
from django.shortcuts import render
from calc.quadratic import quadratic

# Create your views here.

def index(request):
    return render(request, 'index.html')

def reposta(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = request.POST.get('c')

    roots = quadratic(int(a),int(b),int(c))
    return render(request, 'greater.html', roots)