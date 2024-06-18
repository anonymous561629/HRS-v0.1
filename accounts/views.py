from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib import auth
from properties.models import Property, Enquiry

# Custom function
def registration(request, data, user_type):
        username = data['username']
        email_address = data['email-address']
        contact_no = data['contact-no']
        address = data['address']
        password = data['password']
        confirm_password = data['cpassword']
       
        if username == '' or email_address == '' or contact_no == '' or address == '' or password == '' or confirm_password == '':
            messages.error(request, "Please fill all the fields")
            # return HttpResponse('Please fill all the fields') 
        else:
            # check if passwords match
            if password == confirm_password:
            #     # check if username is taken
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username is taken")
                    # return HttpResponse('Username is taken')
                # check if email is being used
                else:
                    if User.objects.filter(email=email_address).exists():
                        messages.error(request, "Email is being used")
                        # return HttpResponse('Email is being used')
                    else:
                        if user_type == 'owner':
                            owner = User(is_owner=True, username=username, email=email_address, contact_no=contact_no, address=address)
                        elif user_type == 'user':
                             owner = User(is_user=True, username=username, email=email_address, contact_no=contact_no, address=address)
                        owner.set_password(password)
                        owner.save()
                        messages.success(request, 'Registered Successfully!')
                        # return HttpResponse('Registered Successfully!')
                        
            else:
                messages.error(request, 'Passwords should match')
                # return HttpResponse('Passwords should match')

def owner_registration(request):
    if request.method == 'POST':
        registration(request, request.POST, 'owner')

        
    return render(request, 'accounts/owner_registration.html')

def user_registration(request):
    if request.method == 'POST':
        registration(request, request.POST, 'user')
    return render(request, 'accounts/user_registration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.error(request, 'Please fill up the fields')
            return redirect('login_user')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'Loggedin Successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')

    return render(request, 'accounts/login.html')

def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Loggedout Successfully')
    return redirect('login_user')

def manage_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email-address']
        contact_no = request.POST['contact-no']
        address = request.POST['address']
        if username == '' or email == '' or contact_no == '' or address == '':
            messages.error(request, 'Please fill up all the fields')
            return redirect('manage_profile')
        else:
            user = User.objects.get(id=request.user.id)
            user.username = username
            user.email = email
            user.contact_no = contact_no
            user.address = address
            user.save()
            messages.success(request, 'Profile updated successfully')
    return render(request, 'accounts/manage_profile.html')

def send_enquiries(request):
    enquiries = Enquiry.objects.filter(user_id=request.user.id)
    context = {
        'enquiries': enquiries,
    }
    return render(request, 'accounts/send_enquiries.html', context)

def recieved_enquiries(request):
    enquiries = Enquiry.objects.filter(property_id__owner_id=request.user.id)
    context = {
        'enquiries': enquiries,
    }
    return render(request, 'accounts/recieved_enquiries.html', context)

def enquiry_details(request, enquiry_id):
    enquiry = Enquiry.objects.get(id=enquiry_id)
    context = {
        'enquiry': enquiry,
    }
    return render(request, 'accounts/enquiry_details.html', context)

def manage_properties(request):
    if request.user.is_authenticated and request.user.is_owner:
        owner_properties = Property.objects.filter(owner_id=request.user.id)
        context = {'owner_properties': owner_properties}
        return render(request, 'accounts/manage_properties.html', context)
    else:
        return redirect('login_user')
    
def delete_property(request, property_id):
    deleted_property = Property.objects.get(id=property_id)
    deleted_property.delete()
    messages.success(request, 'Property deleted successfully')
    return redirect('manage_properties')

def book_property(request, property_id):
    booked_property = Property.objects.get(id=property_id)
    booked_property.delete()
    messages.success(request, 'That property has being booked/rented')
    return redirect('manage_properties')

def update_property(request, property_id):
    updated_property = Property.objects.get(id=property_id)
    context = {
        'updated_property': updated_property,
    }
    return render(request, 'accounts/update_property.html', context)
