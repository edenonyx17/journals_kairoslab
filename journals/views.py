"""Class Based Views"""

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
  )
from .models import journal
from .forms import journalCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
class journalListView(ListView):
    model = journal
    template_name = 'journals/journal_list.html'
    context_object_name = 'journals'

class journalDetailView(LoginRequiredMixin, DetailView):
    model = journal
    template_name = 'journals/journal_detail.html'

class journalCreateView(CreateView):
    model = journal
    template_name = 'journals/create.html'
    form_class = journalCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

class journalUpdateView(LoginRequiredMixin, UpdateView):
    model = journal
    template_name = 'journals/update.html'
    form_class = journalCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

class journalDeleteView(DeleteView):
    model = journal
    template_name = 'journals/delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class AboutPageView(TemplateView):
    template_name = 'journals/about.html'
