from django.shortcuts import render

def new_home(request):
    return render(request, 'main/about.html')