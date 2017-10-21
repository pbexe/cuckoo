from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')

def api(request):
    if request.method == 'POST':
        print(request.POST.get('destination'))
        print(request.POST.get('lat'))
        print(request.POST.get('long'))
    return HttpResponse("OK")