from django.shortcuts import render
from django.http import HttpResponse
from properties.models import Property

def index(request):
    featured_properties = Property.objects.filter(is_featured=True).order_by('-list_date')[:6]
    recent_properties = Property.objects.order_by('-list_date')[:6]
    context = {'recent_properties': recent_properties, 'featured_properties': featured_properties}
    return render(request, 'pages/index.html', context)

