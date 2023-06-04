from django.shortcuts import render

# Create your views here.


def uploadBloge(request):
    return render(request,'upload.html')