from django.shortcuts import render
from home.models import *
from product.models import *


# Create your views here.
def index(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
        'category':category,
        'sub_category':sub_category,
    }

    return render(request,'main/index.html',context)

def aboutus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
    }

    return render(request,'main/about.html',context)

def product(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    product = Product.objects.all().order_by('?')

    page="home"
    context={
        'setting':setting,
        'product':product,
    }
    return render(request,'main/product.html',context)

def faqs(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/FQA.html',context)

def contactus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/contactus.html',context)

def BRAND(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/BRAND.html',context)

def BLOG(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/BLOG.html',context)

def Gallery(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Gallery.html',context)


def Our_Team(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/OurtTeam.html',context)


def Vision_Mission(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Vision-Mission.html',context)

def DirectorDesk(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/director-desk.html',context)


#=====================Service Area=================================
def Architecture(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Architecture.html',context)


def Construction(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Construction.html',context)


def Interior(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Interior.html',context)



def Landscape(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Landscape.html',context)


def Turnkey(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/Turnkey.html',context)


def project(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/project.html',context)