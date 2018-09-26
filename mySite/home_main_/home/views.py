from django.shortcuts import render,HttpResponse
from .form import dummyForm
from CompanyRegistration.models import City ,Company_Registration
import pdb

def index(request):
    data = City.objects.all()
    comp_data = Company_Registration.objects.all()
    # return render(request,'index.html',{})
    # else:
    return render(request,'index.html',{'data':data})


def compare(request):
    if request.method == "POST":
        d = dummyForm(request.POST)
        data = City.objects.all()
        if d.is_valid():
            D = d.save(commit=False)
            city1 = Company_Registration.objects.filter(city__name=D.name)
            # for item in Company_Registration.objects.all():
            return render(request,'index.html',{'data':data,'comp_data':city1})
    else:
        data = City.objects.all()
        return render(request,'index.html',{'data':data})              
        # return HttpResponse("notfound")
    

        