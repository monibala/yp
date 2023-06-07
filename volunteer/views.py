from django.shortcuts import render
from .models import *
# Create your views here.
def volunteer(request):
    res = {}
    res['v'] = volunteer_info.objects.all()
    return render(request, 'volunteer.html',res)
def volunteerdetail(request,id):
    res = {}
    res['d'] = volunteer_info.objects.get(id=id)
    return render(request, 'volunteer-details.html',res)
def becomevolunteer(request):
    if request.method=="POST":
        firstname =request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        zipcode = request.POST['zipcode']
        bv = become_volunteer(firstname=firstname,lastname=lastname,email=email,mobile=mobile,city=city,country=country,address=address,zipcode=zipcode)
        bv.save()
    return render(request ,'become-a-volunteer.html')