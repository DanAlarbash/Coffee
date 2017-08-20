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
	syrup = models.ManyToManyField(Syrup, null=True, blank=True) 
	powder = models.ManyToManyField(Powder,null=True, blank=True) 
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






