from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments
from .models import Doctors
from .forms import BookingForm
from .models import Booking
from django.http import HttpResponseRedirect



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
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request, 'booking.html',dict_form)

def doctors(request):

    dict_doc = {

              'doctor' : Doctors.objects.all() 
    }

    return render(request, 'doctors.html', dict_doc)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)
