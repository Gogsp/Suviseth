import django
from django.conf.urls import url
from django.urls import path
from django.http import request
from SuvisethApp import views
from django.conf import settings
from django.conf.urls.static import static

#TEMPLATE TAGGING
app_name = 'SuvisethApp'

urlpatterns = [
    path('signup',views.signUp,name='signup'),
    path('signin',views.signIn,name='signin'),
    path('client_signup',views.clientSignup,name='client_signup'),
    path('sprovider_signup',views.sproviderSignup,name='sprovider_signup'),
    path('admin_signup',views.adminSignup,name='admin_signup'),
    path('client_signin',views.clientSignin,name='client_signin'),
    path('sprovider_signin',views.sproviderSignin,name='sprovider_signin'),
    path('admin_signin',views.adminSignin,name='admin_signin'),
    path('signout',views.user_logout,name='signout'),
    path('wedding_services',views.weddingServices,name='wedding_services'),
    path('find_partner',views.findPartner,name='find_partner'),

    path('categories',views.categories,name='categories'),
    path('category/<str:category_id>',views.category,name='category'),
    path('add_category',views.add_category,name='add_category'),
    path('edit_category/<str:category_id>',views.edit_category,name='edit_category'),
    path('delete_category/<str:category_id>',views.delete_category,name='delete_category'),

    path('all_service_providers',views.service_providers,name='all_service_providers'),
    path('all_service_provider/<str:sp_id>',views.service_provider,name='service_provider'),
    path('edit_service_provider/<str:sp_id>',views.edit_service_provider,name='edit_service_provider'),
    path('delete_service_provider/<str:sp_id>',views.delete_service_provider,name='delete_service_provider'),

    path('all_customers',views.customers,name='customers'),
    path('customer/<str:c_id>',views.customer,name='customer'),
    path('deactivate_account/<str:c_id>',views.remove_customer,name='remove_customer'),


] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)