from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
from django.contrib.auth.decorators import login_required

# print ('static--', static)

# Create your views here.
@login_required
def index(request):

	print(request.user.is_authenticated)

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

		choice_votes = Choice.objects.get(pk=request.POST.get('vote'))
		choice_votes.votes += 1
		choice_votes.save()

		question_list = Question.objects.all()
		context = {
			'question_list':question_list
		}	


		return render(request,'polls/index.html', context )



	choice_obj_list = Choice.objects.filter(question_id=question_id )
	context = {
		'choice_obj_list':choice_obj_list
	}

	return render(request, 'polls/vote.html',context)




def result(request, question_id):

	#return HttpResponse("Result page %s" % question_id )

	question = Question.objects.get(pk=question_id)
	context={'question':question }
	return render(request,'polls/result.html',context)

