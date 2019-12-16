from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp.models import Donor,NGO,Volunteer,order

def ngoregister(request):
    if request.method == 'POST':
        n_name = request.POST["NGO_name"]
        NGO_num = request.POST["NGO_num"]
        NGO_adrr = request.POST["NGO_addr"]
        NGO_adhaar = request.POST["NGO_adhaar"]
        NGO_email = request.POST["email"]
        pword = request.POST["pword"]

        NGO_info = NGO(NGO_name=n_name,NGO_num=NGO_num,NGO_adrr=NGO_adrr,NGO_adhaar=NGO_adhaar,pword=pword,NGO_Email=NGO_email)
        NGO_info.save()
        return render(request, 'ngo/ngo_login.html')

    else:
        return render(request, 'ngo/ngo-register.html')

def ngologin(request):
    if request.method == 'POST':
        ngo_email = request.POST["nid"]
        pword = request.POST["pword"]
        ngo_info = NGO.objects.get(NGO_Email=ngo_email,pword=pword)
        if ngo_info is not None:
            request.session['ngo'] = ngo_info.NGO_name
            return redirect('ngopage')
    else:
        if not request.session.has_key('ngo'):
            return render(request, 'ngo/ngo_login.html')
        elif request.session.has_key('volunteer'):
            return redirect('volunteerpage')
        elif request.session.has_key('donor'):
            return redirect('donorpage')
        elif request.session.has_key('ngo'):
            return redirect('ngopage')

def ngo(request):
    if request.session.has_key('ngo'):
        n_name = request.session['ngo']
        return render(request, 'ngo/ngopage.html', {"f_name" : n_name})

