from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"home.html")

def show1(request):
    return render(request,"about.html")

def show2(request):
    return render(request,"jobs.html")

def show3(request):
    return render(request,"view_job.html")

def show4(request):
    return render(request,"view_company.html")

def show5(request):
    return render(request,"contact.html")

def show6(request):
    return render(request,"login.html")

def show7(request):
    return render(request,"register.html")
