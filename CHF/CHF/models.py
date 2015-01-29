from django.db import models
from django.contrib.auth.models import User
# USER MANAGEMENT CLASSES
# Change

class Photo(models.Model):
    fileLocation = models.TextField(max_length=255)
    title = models.TextField(max_length=25)
    dateTaken = models.DateTimeField(blank=True, null=True)
    placeTaken = models.TextField(max_length=25, blank=True, null=True)
    caption = models.TextField(max_length=255)

# add upload/download methods to each photo class


class Client(models.Model):
    # REMOVED ALL ATTRIBUTES FOUND IN DJANGO USER CLASS AS WELL AS CLIENT TYPE
    address = models.TextField(max_length=35)
    city = models.TextField(max_length=25)
    state = models.CharField(max_length=2)
    zip = models.TextField(max_length=20)
    securityQuestion = models.TextField(max_length=100)
    securityAnswer = models.TextField(max_length=25)
    phoneNumber = models.TextField(max_length=25)
    photo = models.ForeignKey(Photo, blank=True, null=True)
    user = models.OneToOneField(User)
# add validate data method?


class Manager(Client):
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField(blank=True, null=True)


class Agent(Manager):
    appointment_creation_date = models.DateTimeField()
    appointment_expiration_date = models.DateTimeField(blank=True, null=True)


class Participant(Client):
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField(blank=True, null=True)
    biographical_sketch = models.TextField(max_length=255)
    contact_relationship = models.TextField(max_length=25, blank=True, null=True)
    emergency_contact = models.TextField(max_length=25, blank=True, null=True)
    emergency_contact_phone = models.TextField(max_length=25, blank=True,null=True)


class Admin(Client):
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField(blank=True, null=True)


# END USER MANAGEMENT CLASSES

# Sales/Inventory classes


class Product(models.Model):
    name = models.TextField(max_length=25)
    description = models.TextField(max_length=255)
    category = models.TextField(max_length=25)
    currentPrice = models.DecimalField(max_digits=6, decimal_places=2)
    client = models.ForeignKey(Client)


class Order (models.Model):
    order_date = models.DateTimeField()
    phone = models.IntegerField(max_length=11)
    date_packed = models.DateTimeField(blank=True, null=True)
    date_paid = models.DateTimeField(blank=True, null=True)
    date_shipped = models.DateTimeField(blank=True, null=True)
    tracking_number = models.IntegerField(max_length=25)
    agent = models.ForeignKey(Agent)


class BulkProduct(Product):
    quantity_on_hand = models.IntegerField(max_length=6)


class IndividualProduct(Product):
    quantity_on_hand = models.IntegerField(max_length=6)
    order = models.ForeignKey(Order)


class PersonalProduct(Product):
    quantity_on_hand = models.IntegerField(max_length=6)


class BulkDetail(models.Model):
    quantity = models.IntegerField(max_length=6)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    bulk_product = models.ForeignKey(BulkProduct)
    order = models.ForeignKey(Order)


class PersonalDetail(models.Model):
    order_file = models.TextField(max_length=255)
    personal_product = models.ForeignKey(PersonalProduct)
    order = models.ForeignKey(Order)

# End of Sales/Inventory classes


# ##################START EVENT CLASSES#########################
class Event(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    mapFileName = models.TextField(max_length=100)


class Area(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=300)
    placeNumber = models.IntegerField(max_length=4)
    event = models.ForeignKey(Event)


class SaleItem(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=300)
    lowPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    highPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    area = models.ForeignKey(Area)
    # add method for setPrice()


class Role(models.Model):
    name = models.TextField(max_length=50)
    type = models.TextField(max_length=50)
    area = models.ForeignKey(Area)
    participant = models.ForeignKey(Participant)


class Venue(models.Model):
    name = models.TextField(max_length=30)
    address = models.TextField(max_length=50)
    city = models.TextField(max_length=20)
    state = models.TextField(max_length=2)
    zip = models.IntegerField(max_length=10)
    event = models.ForeignKey(Event)
    # make method for makeReservation()
# ###################END EVENT CLASSES#######################

# Rental and Item Inventory Classes


class Item(models.Model):
    client = models.ForeignKey(Client)
    name = models.TextField(max_length=25)
    description = models.TextField(max_length=255, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    standard_rental_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rentable = models.CharField(max_length=1)
    photo = models.ForeignKey(Photo, blank=True, null=True)


class Rental(models.Model):
    rental_time = models.DateTimeField()
    due_date = models.DateField(max_length=10)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    agent = models.ForeignKey(Agent, null=True, blank=True)


class RentedItem(models.Model):
    condition = models.TextField(max_length=30, null=True, blank=True)
    new_damage = models.TextField(max_length=100, blank=True, null=True)
    damage_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rental = models.ForeignKey(Rental, blank=True, null=True)


class Return(models.Model):
    return_time = models.DateTimeField()
    due_date = models.DateTimeField(null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class WardrobeItem(Item):
    size = models.TextField(max_length=3, null=True, blank=True)
    size_modifier = models.TextField(max_length=20, null=True, blank=True)
    gender = models.TextField(max_length=10, null=True, blank=True)
    color = models.TextField(max_length=15, null=True, blank=True)
    pattern = models.TextField(max_length=30, null=True, blank=True)
    start_year = models.TextField(max_length=10, null=True, blank=True)
    end_year = models.TextField(max_length=10, null=True, blank=True)
    note = models.TextField(max_length=255, null=True, blank=True)
# End rental and item inventory classes
