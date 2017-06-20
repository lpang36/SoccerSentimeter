from django.shortcuts import render

# Create your views here.
def about(request):
	return render(request,'base/about.html',{})
	
def home(request):
	return render(request,'base/home.html',{})