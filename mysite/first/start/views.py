from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def explain(request):
    return render(request, 'explain.html')