from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def home(request):
#     #    return render(request,'home.html',{'emps_name':'XYZ'})
#     #  return HttpResponse('hii i am aman ')

#     template = loader.get_template('home.html')
#     name = {
#         'emp':'XYZ'
#      }
#     return HttpResponse(template.render(name))     

def home1(request):
    #    return render(request,'home.html',{'emps_name':'XYZ'})
    #  return HttpResponse('hii i am aman ')

    template = loader.get_template('home1.html')
    name = {
        'emp':'ABC'
     }
    return HttpResponse(template.render(name))  


def home2(request):
    #    return render(request,'home.html',{'emps_name':'XYZ'})
    #  return HttpResponse('hii i am aman ')

    template = loader.get_template('home2.html')
    name = {
        'emp':'XYZ'
     }
    return HttpResponse(template.render(name))                