from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def registr(request):
    return render(request,'registr.html')