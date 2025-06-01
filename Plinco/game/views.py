from django.shortcuts import render

def home(request):
    return render(request, 'plinko_templates/home.html')
