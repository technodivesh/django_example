from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(verbose_name='Published Date')  # verbose_name is Human Readable name

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		"It returns True if pub_date is in last 24 hrs"
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	# Change name 'WAS PUBLISHED RECENTLY' to 'Published recently?' for admin page on Question page
	was_published_recently.short_description = 'Published recently?'

	# Change True/ False with right check and cross icons
	was_published_recently.boolean = True

	was_published_recently.admin_order_field = 'pub_date'


class Choice(models.Model):

	choice_text = models.CharField(max_length=200)
	question = models.ForeignKey('Question',on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
