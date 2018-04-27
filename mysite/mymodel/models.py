from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Person(models.Model):

	name = models.CharField(max_length=60, verbose_name='Person Name',help_text="Please use Charatater only")
	# help_text will be displayed under Form field

	# It must be tuple of tuples
	SHIRT_SIZES = ( 
		('S','Small'),
		('M','Medium'),
		('L','Large')
	)
	shirt_size = models.CharField(max_length=1,verbose_name = 'Shirt Size', choices=SHIRT_SIZES )
	add_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


# Many to One relationship ---------START
# use ForeignKey
class Manufacturer(models.Model):

	name = models.CharField(max_length=100,verbose_name='Car Company')
	year = models.PositiveIntegerField(validators=[
			MinValueValidator(1950),
			MaxValueValidator(timezone.now().year)
		])

	def __str__(self):
		return self.name


class Car(models.Model):

	car_name = models.CharField(max_length=100)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	year_launch = models.PositiveIntegerField(validators=[
			MinValueValidator(1950),
			MaxValueValidator(timezone.now().year)
		])

	def __str__(self):
		return self.car_name
# Many to One relationship ---------END



# Many to Many relationship --------START
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
# Many to Many relationship --------END

# p1 = Publication.objects.create(title='Pearson')




# Many to Many Relationship with intermediate model----START
class Mperson(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Mperson, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Mperson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

# Many to Many Relationship with intermediate model----END
