from django.views.generic import ListView, DetailView, CreateView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

# allowing users to create their own Cheese models via the UI
# next step is to add the corresponding URL in cheeses/urls.py
class CheeseCreateView(CreateView):
    model = Cheese
    fields = [
        'name',
        'description',
        'country_of_origin',
        'firmness',
    ]
