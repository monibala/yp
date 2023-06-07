from django.conf import settings
from django.shortcuts import render
from home.models import campaign_mgmt, contact_info, event_info, gallery_info, teams
from blog.models import blogs
from volunteer.models import volunteer_info
from django.core.mail import send_mail
from django.contrib import messages as sms
from django.views.decorators.clickjacking import xframe_options_deny
# Create your views here.
def index(request):
    res = {}
    
    res['v'] = volunteer_info.objects.all()
    res['e'] = event_info.objects.all()
    res['el'] = event_info.objects.all().last()
    res['b'] = blogs.objects.all()
    return render(request, 'index-2.html',res)
def events(request):
    res = {}
    res['e'] = event_info.objects.all()
    return render(request, 'events.html',res)

def eventdetail(request,id):
    res = {}
    res['e'] = event_info.objects.get(id=id)
    return render(request, 'events-details.html',res)
def gallery(request):
    res = {}
    res['g'] = gallery_info.objects.all()
    return render(request, 'gallery.html',res)
def history(request):
    return render(request, 'history.html')
def donate(request):
    return render(request, 'donate.html')
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message =request.POST['message']
        c = contact_info(name=name,mobile=mobile,email=email,message=message)
        c.save()
        mg = (f'Name:{name} \n Email:{email} \n Mobile:{mobile} \n Message:{message}')
        send_mail('subject',mg,email,[settings.EMAIL_HOST_USER],fail_silently=False)
        sms.success(request,'Your Message Send Successfully.')
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faq.html')

def team(request):
    data = teams.objects.all()
    context = {'data' : data}
    return render(request, 'team.html' , context)  

def campaign(request):
    res = {}
    res['data'] = teams.objects.all()
    res['c'] = campaign_mgmt.objects.all()
    return render(request, 'campaign.html',res)      
def all_search(request):
    return render(request,'searchnotfound.html')