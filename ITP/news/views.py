from django.shortcuts import render

def new_home(request):
    return render(request, 'news/news_home.html')