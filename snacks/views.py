
from django.views.generic import ListView, DetailView
from .models import Snacks

# Create your views here.

class SnackListView(ListView):
    template_name='snack_list.html'
    model = Snacks

class SnackDetailsView(DetailView):
    template_name='snack_detail.html'
    model = Snacks