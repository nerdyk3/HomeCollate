from django.shortcuts import render,HttpResponse
from .form import dummyForm,dummyForm2
from CompanyRegistration.models import City ,Company_Registration
from PropertyRegistration.models import Property_Registration
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
            Dname = D.name
            city3(Dname)
            city1 = Company_Registration.objects.filter(city__name=D.name).order_by('priceMini')
            # for item in Company_Registration.objects.all():
            return render(request,'index.html',{'data':data,'comp_data':city1})
    else:
        data = City.objects.all()
        return render(request,'index.html',{'data':data})              
        # return HttpResponse("notfound")

def city3(Dname):
    global city4
    city4 = Dname
    return 0


# def result(request):
#     city2 =Property_Registration.objects.filter(Area__name=city4)
#     return render(request,'result.html',{'result':city2})

def about_us(request):
    return render(request,'about-us.html')
def faqs(request):
    return render(request,'FAQs.html')
def partner_with_us(request):
    return render(request,'partner-with-us.html')
def privacy(request):
    return render(request,'privacy.html')
def T_C(request):
    return render(request,'T&C.html')
def why_us(request):
    return render(request,'why-us.html')

def result(request):
    if request.method== "POST":
        dummycompany = dummyForm2(request.POST)
        if dummycompany.is_valid():
            Dummycompany =dummycompany.save(commit=False)
            DummyCompany = Dummycompany.company
            Company_PG =Property_Registration.objects.filter(Company__company=DummyCompany)
            return render(request,'search_result.html',{'Company_PG':Company_PG})
    else:
        return HttpResponse("Please search_resul")