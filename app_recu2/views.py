from django.shortcuts import render
from calc.quadratic import quadratic

def index(request):
    context = {}
    if request.method == 'POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        c = int(request.POST.get('c'))

        roots = quadratic(a, b, c)
        context = roots
    return render(request, 'index.html', context)
