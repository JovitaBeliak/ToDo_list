from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from .forms import CustomUserCreateForm, TaskReviewForm
from .models import Task, CustomUser


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

class TaskDetailView(FormMixin, generic.DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'
    form_class = TaskReviewForm

    def get_success_url(self):
        return reverse('task', kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.task = self.get_object()
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)


class MyTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'my_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(doer=self.request.user)

class SignUpView(generic.CreateView):
    form_class = CustomUserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
