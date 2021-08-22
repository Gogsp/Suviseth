from django.db import models
from django.contrib.auth.models import User
from django.utils import translation

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,null=False)
    description = models.CharField(max_length=200,null=True,blank=True)
    images = models.ImageField(upload_to='category_pics',blank=True)

    def __str_(self):
        return self.name

class Admin(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

     # Additional
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str_(self):
        return self.user.username


class Customer(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional
    DISTRICT = ( 
    ("Ampara", "Ampara"), 
    ("Anuradhapura", "Anuradhapura"),
    ("Badulla","Badulla"),
    ("Baticaloa","Baticaloa"),
    ("Colombo","Colombo"),
    ("Galle","Galle"),
    ("Gampaha","Gampaha"),
    ("Hambantota","Hambantota"),
    ("Jaffna","Jaffna"),
    ("Kalutura","Kalutura"),
    ("Kandy","Kandy"),
    ("Kegalle","Kegalle"),
    ("kilinochchi","kilinochchi"),
    ("Kurunegala","Kurunegala"),
    ("Mannar","Mannar"),
    ("Matale","Matale"),
    ("Matara","Matara"),
    ("Monaragala","Monaragala"),
    ("Mullaitivu","Mullaitivu"),
    ("Nuwara Eliya","Nuwara Eliya"),
    ("Polonnaruwa","Polonnaruwa"),
    ("Puttalam","Puttalam"),
    ("Ratnapura","Ratnapura"),
    ("Trincomalee","Trincomalee"),
    ("Vavuniya","Vavuniya")
    ) 
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    first_name = models.CharField(max_length=150,null=True)
    last_name = models.CharField(max_length=150,null=True)
    date_of_birth = models.DateField()
    mobile_no = models.CharField(max_length=15)
    address = models.TextField(max_length=250, blank=True)
    district = models.CharField(
                max_length=150,
                choices=DISTRICT, 
                null=True)
    

    

    def __str_(self):
        return self.user.username

class ServiceProvider(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

     # Additional 
    DISTRICT = ( 
    ("Ampara", "Ampara"), 
    ("Anuradhapura", "Anuradhapura"),
    ("Badulla","Badulla"),
    ("Baticaloa","Baticaloa"),
    ("Colombo","Colombo"),
    ("Galle","Galle"),
    ("Gampaha","Gampaha"),
    ("Hambantota","Hambantota"),
    ("Jaffna","Jaffna"),
    ("Kalutura","Kalutura"),
    ("Kandy","Kandy"),
    ("Kegalle","Kegalle"),
    ("kilinochchi","kilinochchi"),
    ("Kurunegala","Kurunegala"),
    ("Mannar","Mannar"),
    ("Matale","Matale"),
    ("Matara","Matara"),
    ("Monaragala","Monaragala"),
    ("Mullaitivu","Mullaitivu"),
    ("Nuwara Eliya","Nuwara Eliya"),
    ("Polonnaruwa","Polonnaruwa"),
    ("Puttalam","Puttalam"),
    ("Ratnapura","Ratnapura"),
    ("Trincomalee","Trincomalee"),
    ("Vavuniya","Vavuniya")
    ) 

    company_logo = models.ImageField(upload_to='company_logos',blank=True)
    company_name = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=15)
    district = models.CharField(
                max_length=150,
                choices=DISTRICT,
                null=True)
    categories = models.ManyToManyField(Category,blank=True)
    
    
    def __str_(self):
        return self.company_name

class Package(models.Model):

    PACKAGE_TYPES = (
        ("Single-Service","Single-Service"),
        ("Multiple-Service","Multiple-Service"),
        ("Full-Planner","Full-Planner")
    )

    name = models.CharField(max_length=250)
    type = models.CharField(
                max_length=150,
                choices=PACKAGE_TYPES, 
                null=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    images = models.ImageField(upload_to='package_pics',blank=True)
    price = models.CharField(max_length=50)
    discount_rate = models.IntegerField(blank=True,null=True)
    service_provider = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)

    def __str_(self):
        return self.name

# class Payment(models.Model):
#     card_no = models.CharField(max_length=50)
#     cardholder_name =models.CharField(max_length=150)
#     cvv = models.BigIntegerField()
#     amount = models.CharField(max_length=50)
#     exp_date = models.DateField()

#     def __str_(self):
#         return self.card_no