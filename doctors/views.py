from django.shortcuts import render

# Create your views here.
def doctors_list(request):
    return render(request, 'doctors/doctors.html')