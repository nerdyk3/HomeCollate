from django.shortcuts import render
from .forms import enquiry_web_form

def enquiry(request):
	if request.method == "POST":
		d = enquiry_web_form(request.POST)
		if d.is_valid():
			D= d.save(commit=False)
			D.save()
			return render(request,'index.html',{})
	else:
		d = enquiry_web_form()
		return render(request,'enquiry_user.html',{'d':d})