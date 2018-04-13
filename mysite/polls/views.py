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

	question_obj = Question.objects.get(pk=question_id)

	context = {
		'question_obj':question_obj
	}
	return render(request,'polls/detail.html', context)


def vote(request, question_id):
	# return HttpResponse("Vote page %s" % question_id )

	if request.method == 'POST':


		print (request.POST['vote'])
		return HttpResponse("Vote DOne %s" % request.POST )











	choice_obj_list = Choice.objects.filter(question_id=question_id )
	context = {
		'choice_obj_list':choice_obj_list
	}

	return render(request, 'polls/vote.html',context)




def result(request, question_id):
	return HttpResponse("Result page %s" % question_id )