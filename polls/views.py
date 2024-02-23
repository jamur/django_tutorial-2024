from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.urls import reverse

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)    
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
                  
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

def poll_create(request):
    if request.method == 'POST':
        # Process the form data
        # and create a new poll
        return redirect('polls:poll_list')
    else:
        # Render the form
        return render(request, 'polls/poll_create.html')

def poll_update(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'POST':
        # Process the form data
        # and update the poll
        return redirect('polls:poll_detail', pk=poll.pk)
    else:
        # Render the form
        return render(request, 'polls/poll_update.html', {'poll': poll})

def poll_delete(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'POST':
        # Delete the poll
        return redirect('polls:poll_list')
    else:
        return render(request, 'polls/poll_delete.html', {'poll': poll})
