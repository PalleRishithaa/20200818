from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def home(requests):
    return HttpResponse('<h1>This is my page</h1><ul><li>Name:Rishithaa Palle</li><li>Roll.No: 1602-18-737-031</li></ul>')
def aboutus(requests):
    return HttpResponse('<h1>I am persuing B.E IT in vasavi college of engineering</h1><ul><li>Name:Rishithaa Palle</li><li>Roll.No: 1602-18-737-031</li></ul>')
def myhobbies(requests):
    return HttpResponse('<ul><li>Name:Rishithaa Palle</li><li>Roll.No: 1602-18-737-031</li></ul><h1>MY Hobbies:</h1><ul><li>Watching TV</li><li>Painting</li></ul>')


