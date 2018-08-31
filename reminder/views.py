from django.shortcuts import render

# MVC --> MTV. view in django is controller

# Create your views here.
def manage(request):
   zipcodes = range(10001,10010)
   return render(request, 'manage.html', {'zipcodes': zipcodes})