from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#the buidings up for residence


class Residence(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    num_rooms = models.IntegerField()
    sex = models.TextField(blank=True)
    classification = models.TextField(blank=True)
    athlete = models.TextField(blank=True)
    sport = models.TextField(blank=True)
    honors = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#the floors in the residence halls


class Floors(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    floor = models.IntegerField()
    num_rooms = models.IntegerField()
    sex = models.TextField(blank=True)
    Eligibility2 = models.TextField(blank=True)
    Eligibility3 = models.TextField(blank=True)

    def __str__(self):
        return self.residence.name + ' floor ' + str(self.floor)


class Rooms(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floors, on_delete=models.RESTRICT)
    suit_num = models.IntegerField()
    room_letter = models.CharField(max_length=1)
    Availability = models.BooleanField(default=True)
    num_rooms = models.IntegerField()
    sport = models.TextField(blank=True)
    staff = models.BooleanField(blank=True)
    Eligibility3 = models.TextField(blank=True)
    occupant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.residence.name) + ' suit/room ' + str(self.suit_num) + self.room_letter


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.TextField()
    sex = models.TextField()
    sport = models.TextField(blank=True)
    honors = models.TextField()
    age = models.IntegerField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.user.last_name


class MySlide(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name







