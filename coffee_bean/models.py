from django.db import models

class Bean(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=1,max_digits=3)


class Syrups(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=1,max_digits=3)

class Powder(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=1,max_digits=3)

class Roast(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=1,max_digits=3)
