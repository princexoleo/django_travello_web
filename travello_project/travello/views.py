from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination() #object 1
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps!'
    dest1.img   ='destination_1.jpg'
    dest1.price = 700
    dest1.offer = False 
    #object 2
    dest2 = Destination()
    dest2.name = 'Mymensingh'
    dest2.desc = 'The beautiful amazing city of Bangladesh!'
    dest2.img   ='destination_2.jpg'
    dest2.price = 600
    dest2.offer = True 
    #object 3
    dest3 = Destination()
    dest3.name = 'Dhaka'
    dest3.desc = 'The city that never sleeps and always busy!'
    dest3.img   ='destination_3.jpg'
    dest3.price = 900
    dest3.offer = False 
    
    dests =[dest1, dest2, dest3]
    return render(request,'travello/index.html',{'dests':dests,'title':'Travello'})
