from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.
def index(request):

	question_list = Question.objects.all()

	context = {
		'question_list':question_list
	}
	return render(request, 'polls/index.html', context )
	# return HttpResponse("Hello")


def detail(request, question_id):
	return HttpResponse("Detail page")


def vote(request, question_id):
	return HttpResponse("Vote page %s" % question_id )


def result(request, question_id):
	return HttpResponse("Result page %s" % question_id )