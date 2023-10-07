from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

person = {
    "name" : "akhil",
    "age" : 22,
    "place" : "Thiruvalla"
}

number = {
    "num" :  0,
    "numar" : [1,2,3,4,5,6,7,8],
    "fruitsar": ["apple","orange","banana"]
}

def index(request):
    return render(request ,"index.html",number)

def about(request):
    return render(request, "about.html" )

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')
