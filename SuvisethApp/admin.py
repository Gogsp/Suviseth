from django.contrib import admin
from SuvisethApp.models import Admin, Category,Customer, Package,ServiceProvider

# Register your models here.
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(ServiceProvider)
admin.site.register(Category)
admin.site.register(Package)