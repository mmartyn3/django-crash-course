from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

# allowing users to create their own Cheese models via the UI
# next step is to add the corresponding URL in cheeses/urls.py
class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'country_of_origin', 'firmness',]

    def form_valid(self, form):
        """Override the default form_valid method to insert creator field
            after the form has been validated. There is no need to
            validate the creator since it is assigned by our code, not
            a form input by the User."""
        form.instance.creator = self.request.user
        return super().form_valid(form)
