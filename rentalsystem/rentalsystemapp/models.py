from django.db import models
import uuid
from django.contrib.auth.models import User


def uuid_generate():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    reference_id=models.CharField(max_length=32,unique=True , default=uuid_generate)
    created_by=models.ForeignKey(User,on_delete=models.PROTECT, db_column ="created_by", null=True, related_name="+")
    updated_by=models.ForeignKey(User,on_delete=models.PROTECT,db_column="updated_by", null=True, related_name="+")
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)
    is_delete=models.BooleanField(default=False)
    

    class Meta:
        abstract = True

class Customer(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    picture=models.ImageField(null=True)
    mobile_number=models.CharField(max_length=100)
    starting_point=models.DateTimeField(blank=True)
    Ending_point=models.DateTimeField(blank=True)
    
    class Meta:
        db_table = "Customer"
        

class Driver(models.Model):
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
    ]
    VERIFICATION_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    picture=models.ImageField(null=True, blank=False)
    mobile_number=models.CharField(max_length=100)
    vechile_type=models.CharField(choices=VEHICLE_CHOICES)
    picture=models.ImageField(null=False, blank=False)
    lincense=models.ImageField(null=False, blank=False)
    verification_status = models.CharField(max_length=10, choices=VERIFICATION_CHOICES, default='pending')
    
    class Meta:
        db_table = "Driver"
        

    

    


