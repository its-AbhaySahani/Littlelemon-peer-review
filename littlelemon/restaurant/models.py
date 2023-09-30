from django.db import models


# Create your models here.
class Booking(models.Model):
   name = models.OneToOneField(to="Menu", on_delete=models.CASCADE, to_field="name")
   amount = models.IntegerField(default=0)

   def __str__(self):
      return self.name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200, primary_key=True)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')
   img = models.CharField(max_length=20, null=True)

   def __str__(self):
      return self.name
   