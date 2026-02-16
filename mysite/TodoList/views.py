from django.shortcuts import render
from django.views import generic

from .models import Task

# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_tasks": Task.objects.count(),
        "num_tasks_finished": Task.objects.filter(status='u').count(),
        "num_tasks_vykdoma": Task.objects.filter(status='v').count(),
        "num_visits": num_visits,
    }

    return render(request, template_name='index.html', context=context)

class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'
    paginate_by = 3

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'
