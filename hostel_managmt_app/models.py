from django.db import models

class HostelFeeItem(models.Model):
    feeid = models.AutoField(primary_key=True)  
    stdid = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentdate = models.DateField()           
    duedate = models.DateField()              
    status = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"Fee ID: {self.feeid}, Student ID: {self.stdid}, Amount: {self.amount}"
    

class HostelItem(models.Model):
    hostelid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    totalflr = models.IntegerField()
    totalrooms = models.IntegerField()
    totalstaff = models.IntegerField()
    
    def __str__(self):
        return f"{self.name or 'Unnamed Hostel'} (ID: {self.hostelid})"


class StudentItem(models.Model):
    stdid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    contactnum = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    parentname = models.CharField(max_length=100)
    parentnum = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    admissiondate = models.DateField(null=True, blank=True)
    floornum = models.IntegerField(null=True, blank=True)
    roomnum = models.IntegerField()

    def __str__(self):
        return f"{self.name} (ID: {self.stdid})"
    
class Room(models.Model):
    hostelid = models.IntegerField(null=True, blank=True) 
    floornum = models.IntegerField()
    roomnum = models.IntegerField()
    capacity = models.IntegerField()
    currentoccupy = models.IntegerField()
    roomtype = models.CharField(max_length=20)

    def __str__(self):
        return f"Room {self.roomnum}, Floor {self.floornum}, Type: {self.roomtype}"
