from django.shortcuts import render,HttpResponse

# Create your views here.
def myviews(request):
    return HttpResponse('hello brother')