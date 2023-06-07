from django.shortcuts import render
from about.models import about_us

from volunteer.models import volunteer_info

# Create your views here.
def about(request):
    res = {}
    res['v'] = volunteer_info.objects.all()
    res['ab'] = about_us.objects.all()
    return render(request, 'about.html',res)