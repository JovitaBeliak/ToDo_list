from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_tasks": Task.objects.count(),
        "num_tasks_finished": Task.objects.filter(status='u').count(),
        "num_tasks_overdue": Task.objects.filter(status='o').count(),
        "num_visits": num_visits,
    }

    return render(request, template_name='index.html', context=context)
