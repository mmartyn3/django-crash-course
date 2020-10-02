from django.urls import path
from . import views


app_name = "cheeses"
urlpatterns = [
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list',
    ),
    # this path allows users to create their own Cheeses via the UI
    # next step - create a new template in templates/cheeses/cheese_form.html
    path(
        route='add/',
        view=views.CheeseCreateView.as_view(),
        name='add',
    ),
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail',
    ),
]
