from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp.models import Donor,NGO,Volunteer,order

def vlogin(request):
    if request.method == 'POST':
        v_email = request.POST["vid"]
        pword = request.POST["vpass"]
        vinfo = Volunteer.objects.get(v_Email=v_email,pword=pword)
        if vinfo is not None:
            dd = {'f_name':vinfo.f_name,'id':vinfo.id}
            request.session['volunteer'] = dd
            return redirect('volunteerpage')
    else:
        if request.session.has_key('volunteer'):
            return redirect('volunteerpage')
        elif request.session.has_key('donor'):
            return redirect('donorpage')
        elif request.session.has_key('ngo'):
            return redirect('ngopage')
        else:
            return render(request, 'volunteer/volunteer_login.html')


def vregister(request):
    if request.method == 'POST':
        f_name = request.POST["f_name"]
        l_name = request.POST["l_name"]
        v_num = request.POST["v_num"]
        v_adrr = request.POST["v_addr"]
        v_adhaar = request.POST["v_adhaar"]
        v_email = request.POST["email"]
        pword = request.POST["pword"]

        v_info = Volunteer(f_name=f_name,l_name=l_name,v_num=v_num,v_adrr=v_adrr,v_adhaar=v_adhaar,pword=pword,v_Email=v_email)
        v_info.save()
        return redirect('volunteerlogin')

    else:
        if request.session.has_key('volunteer'):
            return redirect('volunteerpage')
        elif request.session.has_key('donor'):
            return redirect('donorpage')
        elif request.session.has_key('ngo'):
            return redirect('ngopage')
        else:
            return render(request, 'volunteer/volunteer-register.html')

def volunteer(request):
    if request.session.has_key('volunteer'):
        dd = request.session['volunteer']
        ol = order.objects.all()
        dl = Donor.objects.all()
        
        return render(request, 'volunteer/volunteer_page.html', {"dd" : dd,'ol':ol,'dl':dl})

def accept(request,id):
    if request.session.has_key('volunteer'):
        vinfo = order.objects.get(id=id)
        vinfo.volunteer_id=id
        vinfo.save()
        return redirect('volunteerpage')

    


