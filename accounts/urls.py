from django.urls import path
from . import views

urlpatterns = [
    path('owner_registration', views.owner_registration, name='owner_registration'),
    path('user_registration', views.user_registration, name='user_registration'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('manage_profile', views.manage_profile, name='manage_profile'),
    path('send_enquiries', views.send_enquiries, name='send_enquiries'),
    path('recieved_enquiries', views.recieved_enquiries, name='recieved_enquiries'),
    path('recieved_enquiries/enquiry_details/<int:enquiry_id>', views.enquiry_details, name='enquiry_details'),
    path('manage_properties', views.manage_properties, name='manage_properties'),
    path('manage_properties/delete/<int:property_id>', views.delete_property, name='delete_property'),
    path('manage_properties/book/<int:property_id>', views.book_property, name='book_property'),
    path('manage_properties/update/<int:property_id>', views.update_property, name='update_property'),
]