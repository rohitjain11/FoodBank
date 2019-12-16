from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp.models import Donor,NGO,Volunteer,order

def dregister(request):
    if request.method == 'POST':
        f_name = request.POST["f_name"]
        l_name = request.POST["l_name"]
        h_name = request.POST["h_name"]
        d_num = request.POST["d_num"]
        d_adrr = request.POST["d_addr"]
        d_adhaar = request.POST["d_adhaar"]
        d_email = request.POST["email"]
        pword = request.POST["pword"]

        d_info = Donor(f_name=f_name,l_name=l_name,hotel_name=h_name,d_num=d_num,d_adrr=d_adrr,d_adhaar=d_adhaar,pword=pword,d_Email=d_email)
        d_info.save()
        return render(request, 'donor/donor-login.html')

    else:
        if request.session.has_key('volunteer'):
            return redirect('volunteerpage')
        elif request.session.has_key('donor'):
            return redirect('donorpage')
        elif request.session.has_key('ngo'):
            return redirect('ngopage')
        else:
            return render(request, 'donor/donor-register.html')


def dlogin(request):
    if request.method == 'POST':
        d_email = request.POST["email"]
        pword = request.POST["pword"]
        try:
            d_info = Donor.objects.get(d_Email=d_email,pword=pword)
        except:
            return render(request, 'donor/donor-login.html',{"msg":"invalid"})
        if d_info is not None:
            dd = {'f_name':d_info.f_name,'id':d_info.id}
            request.session['donor'] = dd
            return redirect('donorpage')

    else:
        if request.session.has_key('volunteer'):
            return redirect('volunteerpage')
        elif request.session.has_key('donor'):
            return redirect('donorpage')
        elif request.session.has_key('ngo'):
            return redirect('ngopage')
        else:
            return render(request, 'donor/donor-login.html')


def donor(request):
    if request.session.has_key('donor'):
        dd = request.session['donor']
        return render(request, 'donor/donor_page.html', {"dd" : dd}) 

def donate(request):
    if request.method == 'POST':
        donor_id = request.POST["donor_id"]
        donor = Donor.objects.get(id=donor_id)
        food_name = request.POST["food_name"]
        food_qty = request.POST["food_qty"]
        order_info = order(food_name=food_name,food_qty=food_qty,donor_id=donor)
        order_info.save()

        msg='order success'
        dd = request.session['donor']
        return render(request, 'donor/donor_page.html', {"dd" : dd,'msg':msg})
    else:
        return redirect('donorpage')

