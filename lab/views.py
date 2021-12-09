from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from lab.models import *

def main(request):
    tst=test.objects.all()
    paginator = Paginator(tst, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(request,"main.html",{'page':page,'count':paginator.count})

def bookingss(request,id):
    obj=test.objects.get(id=id)
    return render(request,"booking.html",{'name':obj})

def booking(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        date=request.POST['date']
        tes=request.POST['test']
        message=request.POST['message']
        s=bookings(name=name,email=email,phone=phone,age=age,date=date,test=tes,message=message)
        s.save()
        return redirect('/')
    return render(request,"booking.html")

def mybooking(request):
    obj=None
    number=None
    if request.method=="POST":
        number=request.POST['number']
    obj=bookings.objects.filter(phone=number).order_by('-date')
    return render(request,"mybook.html",{'mine':obj})

def delete(request,id):
    obj=bookings.objects.get(id=id)
    obj.delete()
    return redirect('mybooking')

def about(request):
    return render(request,"aboutus.html")

def search(request):
    query=None
    obj=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        obj=test.objects.all().filter(Q(test_name__contains=query)|Q(description__contains=query))
    return render(request,"search.html",{'obj':obj,'query':query})