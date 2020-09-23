from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """We can use get_context_data to insert data into Django templates."""
        context = super().get_context_data(**kwargs)
        #context['my_statement'] = "Nice to see you!"
        context['favourite_football_club'] = "Leeds United FC"
        return context

    def say_bye(self):
        """We can also use methods to insert data into Django templates."""
        return "Goodbye"
