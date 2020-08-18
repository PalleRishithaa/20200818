from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def home(requests):
    return HttpResponse('<h1>This is my page</h1>')
def aboutus(requests):
    return HttpResponse('<h1>I am persuing B.E IT in vasavi college of engineering</h1>')
def myhobbies(requests):
    return HttpResponse('<h1>MY Hobbies<h3><ul><li>Watching TV</li><li>Painting</li></ul></h3></h1>')


