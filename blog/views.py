from django.shortcuts import redirect, render
from .models import blogs

# Create your views here.
def blog(request):
    data = blogs.objects.all()
    context = {'data':data}
    return render (request, 'blog.html' , context)

def blogdetail(request,id):
    res = {}
    res['d'] = blogs.objects.get(id=id)
    return render(request, 'blog-details.html',res)
from django.db.models import Q
def search(request):
    res = {}
    if request.method=="POST":
        search = request.POST['search']
        s = (Q(title__contains=search) | Q(desc__contains=search) | Q(date__contains=search))
        s_res = blogs.objects.filter(s)
        if len(s_res)>0:
            res = {'data':s_res}
            return render(request,'blog.html',res)
        else:
            return render(request,'searchnotfound.html')