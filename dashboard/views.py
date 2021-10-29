from django.shortcuts import render

def index(request):
    resp = render(request, 'dashboard/index.html')
    return resp