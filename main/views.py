from django.shortcuts import render

# Create your views here.

def HomePageView(request):
    context={}
    return render(request, 'main/home.html', context)