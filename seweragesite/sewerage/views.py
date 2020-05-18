from django.shortcuts import render
from .models import Controller
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'controllers': Controller.objects.all(),
        'title': 'Home'
    }
    return render(request, 'sewerage/home.html', context)

def about(request):
    return render(request, 'sewerage/about.html', { 'title': 'About'})


class ControllerListView(ListView):
    model = Controller
    template_name = 'sewerage/home.html'
    context_object_name = 'controllers'
    ordering = ['-status']
    paginate_by = 5

class ControllerDetailView(DetailView):
    model = Controller

class ControllerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Controller
    success_url = '/'
    def test_func(self):
        controller = self.get_object()
        if self.request.user == controller.owner:
            return True
        return False
            

class ControllerCreateView(LoginRequiredMixin, CreateView):
    model = Controller
    fields = ['controller_x', 'controller_y','status']

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)

class ControllerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Controller
    fields = ['status']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        controller = self.get_object()
        if self.request.user == controller.owner:
            return True
        return False
            

