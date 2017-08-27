from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Bean(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=3,max_digits=5)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee_bean:bean_detail", kwargs={"slug":self.slug})


def bean_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = Bean.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(bean_slug,sender=Bean)



class Syrup(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=3,max_digits=5)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee_bean:syrup_detail", kwargs={"slug":self.slug})


def syrup_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = Syrup.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(bean_slug,sender=Syrup)

class Powder(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=3,max_digits=5)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee_bean:powder_detail", kwargs={"slug":self.slug})

def powder_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = Powder.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(bean_slug,sender=Powder)


class Roast(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=3,max_digits=5)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee_bean:roast_detail", kwargs={"slug":self.slug})

def roast_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = Roast.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(roast_slug,sender=Roast)






class Coffee(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=20, unique=True)
	bean = models.ForeignKey(Bean)
	roast = models.ForeignKey(Roast)  
	syrup = models.ManyToManyField(Syrup, blank=True) 
	powder = models.ManyToManyField(Powder, blank=True) 
	water = models.FloatField() 
	foam = models.FloatField()
	milk = models.BooleanField(default=False)
	shots = models.PositiveIntegerField()
	extra_instructions = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=3,max_digits=5, null=True)
	slug = models.SlugField(unique=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee_bean:coffee_detail", kwargs={"slug":self.slug})

def coffee_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = Coffee.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(coffee_slug,sender=Coffee)


class City(models.Model):
	name = models.CharField(max_length=15)
	slug = models.SlugField(unique=True, null=True)

	def __str__(self):
			return self.name

	def get_absolute_url(self):
		return reverse("coffee_bean:city", kwargs={"slug":self.slug})

def city_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = City.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(city_slug,sender=City)




class Address(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=15)
	city = models.ForeignKey(City)
	block = models.CharField(max_length=15)
	avenue = models.PositiveIntegerField(null=True, blank=True)
	street = models.CharField(max_length=15)
	building_number = models.PositiveIntegerField()
	floor = models.CharField(max_length=15, null=True, blank=True)
	apt_number = models.CharField(max_length=15, null=True, blank=True)
	extra_instructions = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True, null=True)

	def __str__(self):
			return self.name

	def full_address(self):
		address = ""
		
		address += "%s "%self.city.name

		address = "%s "%self.block

		avenue = ""
		if self.avenue:
			avenue = self.avenue
		address += "%s "%avenue
		
		address += "%s "%self.street

		address += "%s "%self.building_number


		building_number = self.building_number
		address += "%s "%building_number
		
		floor = ""
		if self.floor:
			floor = self.floor
		address += "%s "%floor
		
		apt_number = ""
		if self.apt_number:
			apt_number = self.apt_number
		address += "%s "%apt_number

		return address




	def get_absolute_url(self):
		return reverse("coffee_bean:address", kwargs={"slug":self.slug})

def address_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		# instance.slug=create_slug(instance)
		slug = slugify(instance.name)
		qs = Address.objects.filter(slug=slug)
		exists = qs.exists()
		if exists:
			slug = "%s-%s" % (slug,instance.id)
		instance.slug = slug
		instance.save()

post_save.connect(address_slug,sender=Address)






