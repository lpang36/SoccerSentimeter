from django.shortcuts import render
from team.models import Team

# Create your views here.
def about(request):
	return render(request,'base/about.html',{})
	
def home(request):
	return render(request,'base/home.html',{})
	
def compare(request):
	teams = Team.objects.all()
	return render(request,'base/compare.html',{'teams': teams})