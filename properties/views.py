from django.shortcuts import render, redirect
from .forms import AddPropertyForm
from django.contrib import messages
from .models import Property, Enquiry

def properties(request):
    properties = Property.objects.all()[:6]
    context = {
        'properties': properties,
    }
    return render(request, 'properties/properties.html', context)

def property(request, property_id):
    if request.method == "POST":
        user_id = request.user
        enquiry_message = request.POST['message']
        property = Property.objects.get(id=property_id)
        if enquiry_message == '':
            messages.error(request, 'Please enter your message')
            return redirect('property', property_id=property_id)
        else:
            # If same user sends an enquiry for a same property twice
            enq = Enquiry.objects.filter(user_id=user_id, property_id=property_id).exists()
            if enq:
               messages.error(request, 'You already made an enquiry for this property')
               return redirect('property', property_id=property_id)
            else:
                enquiry = Enquiry(property_id=property, user_id=user_id, message=enquiry_message)
                enquiry.save()  
                messages.success(request, 'Enquiry sends successfully')
                return redirect('property', property_id=property_id)
    else:
        property = Property.objects.get(id=property_id)
        context = {
            'property': property,
        }
        return render(request, 'properties/property.html', context)

def add_property(request):
    form = AddPropertyForm()
    if request.method == 'POST':
        form = AddPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner_id = request.user
            property.save()
            messages.success(request, 'Property added successfully')
    context = {'form': form}
    return render(request, 'properties/add_property.html', context)

def search_property(request):
    user_search = request.GET['search_property'] 
    user_searched_property = Property.objects.filter(address__iexact=user_search)
    context = {
        'user_searched_property': user_searched_property,
    }
    return render(request, 'properties/search_property.html', context)