from django.db import models



class Laptop(models.Model):
    var_name = models.CharField(max_length=20)
    year_of_manufact = models.IntegerField()
    price = models.IntegerField()
    choice = [('pune', 'PUNE'),('mumbai', 'MUMBAI'), ('begluru', 'BENGLURU'), ('delhi', 'DELHI')]
    outlet = models.CharField(max_length=20, choices=choice)

