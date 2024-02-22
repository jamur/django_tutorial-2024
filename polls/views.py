from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll

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
