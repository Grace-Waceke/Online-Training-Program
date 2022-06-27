from .models import Community
from .forms import Community_registration_form
from django.shortcuts import render
# Create your views here.
def communities(request):
  if request.method=="POST":
    form=Community_registration_form(request.POST,request.files)
    if form.is_valid():
      form.save()
    else:
      print(form.errors())
  else:
    form=Community_registration_form()
  return render(request,"community.html",{"form":form})

