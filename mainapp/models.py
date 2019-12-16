from django.db import models

# Create your models here.
class Donor(models.Model):
    f_name =models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    hotel_name = models.CharField(max_length=64)
    d_num = models.CharField(max_length=64)
    d_adrr = models.CharField(max_length=64)
    d_adhaar = models.CharField(max_length=64)
    pword = models.CharField(max_length=64)
    d_Email = models.EmailField()

class NGO(models.Model):
    NGO_name =models.CharField(max_length=64)
    NGO_num = models.CharField(max_length=10)
    NGO_adrr = models.CharField(max_length=64)
    NGO_adhaar = models.CharField(max_length=16)
    pword = models.CharField(max_length=64)
    NGO_Email = models.EmailField()

class Volunteer(models.Model):
    f_name =models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    v_num = models.CharField(max_length=64)
    v_adrr = models.CharField(max_length=64)
    v_adhaar = models.CharField(max_length=64)
    pword = models.CharField(max_length=64)
    v_Email = models.EmailField()

class order(models.Model):
    food_name =models.CharField(max_length=64)
    food_qty = models.CharField(max_length=64)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True)
    volunteer_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True)
    ngo_id = models.ForeignKey(NGO, on_delete=models.CASCADE, null=True)