from django.db import models
from datetime import datetime
from accounts.models import User

class Property(models.Model):
    property_title = models.CharField(max_length=200)
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    rooms = models.IntegerField()
    price = models.IntegerField()
    garage = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    sqft = models.DecimalField(max_digits=5, decimal_places=1)
    is_featured = models.BooleanField(default=False)
    booked = models.BooleanField(default=False)
    main_image = models.ImageField(upload_to='photos/')
    image_1 = models.ImageField(upload_to='photos/')
    image_2 = models.ImageField(upload_to='photos/')
    image_3 = models.ImageField(upload_to='photos/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Amenities
    wifi = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    elevator_access = models.BooleanField(default=False)

    def __str__(self):
        return self.property_title
    
class Enquiry(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    enquiry_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.message