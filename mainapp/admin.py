from django.contrib import admin
from mainapp.models import Donor, NGO, Volunteer, order
# Register your models here.


class AdminDonor(admin.ModelAdmin):
    list_display=['f_name','l_name','hotel_name','d_num','d_adrr','d_adhaar','pword','d_Email']


class AdminNGO(admin.ModelAdmin):
    list_display=['NGO_name','NGO_num','NGO_adrr','NGO_adhaar','pword','NGO_Email',]

class AdminVolunteer(admin.ModelAdmin):
    list_display=['f_name','l_name','v_num','v_adrr','v_adhaar','pword','v_Email']

class AdminOrder(admin.ModelAdmin):
    list_display=['food_name','food_qty','donor_id','volunteer_id','ngo_id']




admin.site.register(Donor,AdminDonor)
admin.site.register(NGO,AdminNGO)
admin.site.register(Volunteer,AdminVolunteer)
admin.site.register(order,AdminOrder)