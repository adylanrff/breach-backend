from django.db import models


class Place(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=200)
  description = models.TextField()
  location = models.TextField()
  image_url = models.CharField(max_length=200, null=True)

  class Meta:
      ordering = ('created',)

# Journey 
class Journey(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  duration = models.IntegerField()
  place = models.ManyToManyField(Place)
  image_url = models.CharField(max_length=200, null=True)
  
  class Meta:
      ordering = ('created',)

#Users 
class User(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=200)
  journey = models.ManyToManyField(Journey)
  
  class Meta:
      ordering = ('created',)

#Vouchers 
class Voucher(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=200)
  discount = models.CharField(max_length=200)
  description = models.TextField()
  code = models.CharField(max_length=10)
  owner = models.ForeignKey(User, related_name='voucher', on_delete=models.CASCADE)
  image_url = models.CharField(max_length=200, null=True)
  category = models.CharField(max_length=10, choices=[(0,"Bronze"), (1,"Silver"), (2,"Gold"), (3,"Platinum")])

  class Meta:
      ordering = ('created',)