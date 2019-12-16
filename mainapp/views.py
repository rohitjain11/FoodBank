from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Donor,NGO,Volunteer,order
# Create your views here.
def home_page(request):
    return render(request, 'mainapp/home-page.html')

#for login type page        
def logintype(request):
    if request.session.has_key('volunteer'):
        return redirect('volunteerpage')
    elif request.session.has_key('ngo'):
        return redirect('ngopage')
    elif request.session.has_key('donor'):
        return redirect('donorpage')
    else:
        return render(request, 'mainapp/login_type.html')

#register type
def registertype(request):
    if request.session.has_key('volunteer'):
        return redirect('volunteerpage')
    elif request.session.has_key('ngo'):
        return redirect('ngopage')
    elif request.session.has_key('donor'):
        return redirect('donorpage')
    else:
        return render(request, 'mainapp/register-type.html')


def logout(request):
    if request.session.has_key('volunteer'):
        del request.session['volunteer']
    if request.session.has_key('donor'):
        del request.session['donor']
    if request.session.has_key('ngo'):
        del request.session['ngo']
    return redirect('home')








