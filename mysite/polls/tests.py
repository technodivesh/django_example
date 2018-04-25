from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone

from .models import Question

# 

class QuestionModelTest(TestCase):

	def test_was_published_recently_with_future_date(self):
		"""was_published_recently should return False if publish date is in Future"""

		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)


	def test_was_published_recently_with_recent_date(self):
		"""was_published_recently should return True if publish date is last 24 hrs"""

		time = timezone.now() + datetime.timedelta(hours=-5)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)
