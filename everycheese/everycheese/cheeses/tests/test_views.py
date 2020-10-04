import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse

from .factories import CheeseFactory, UserFactory
from ..models import Cheese
from ..views import CheeseListView, CheeseDetailView


# connect pytest to the database
pytestmark = pytest.mark.django_db

#Rather than write user = UserFactory() in each test function, we’re going to create a test fixture.
@pytest.fixture
def user():
    return UserFactory()

def test_good_cheese_list_view_expanded(rf):
    # Determine the URL
    url = reverse("cheeses:list")
    # rf is pytest shortcut to django.test.RequestFactory
    # We generate a request as if from a user accessing
    # the cheese list view
    request = rf.get(url)
    # Call as_view() to make a callable object
    # callable_obj is analogous to a function-based view
    callable_obj = CheeseListView.as_view()
    # Pass in the request into the callable_obj to get an
    # HTTP response served up by Django
    response = callable_obj(request)
    # Test that the HTTP response has 'Cheese List' in the
    # HTML *and* that it has a 200 response code. A better name
    # for this would have been assertContainsAndCheckStatus
    assertContains(response, 'Cheese List')

"""
less verbose version of the above test...

def test_good_cheese_list_view(rf):
    # Get the request
    request = rf.get(reverse("cheeses:list"))
    # Use the request to get the response
    response = CheeseListView.as_view()(request)
    # Test that the response is valid
    assertContains(response, 'Cheese List')
"""

def test_good_cheese_detail_view(rf):
    # order some cheese from the CheeseFactory
    cheese = CheeseFactory()
    # Make a request for our new cheese
    url = reverse("cheeses:detail",
        kwargs={'slug':cheese})
    request = rf.get(url)

    # Use the request to get a response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    #Test that the response is valid
    assertContains(response, cheese.name)

def test_good_cheese_create_view(client, user):
    # Make the client autenticate themselves
    client.force_login(user)
    #Specify the URL of the view
    url = reverse("cheeses:add")
    # Use the client to make the request
    response = client.get(url)
    # Test that the response is valid
    assert response.status_code == 200

def test_cheese_list_contains_2_cheeses(rf):
    """
    Test the Cheese List View.
    A good thing to test is whether the list view response contains a couple
    of object’s names. For that, we’ll need to add a few kinds of cheese. Then
    look inside the Cheese List response and check that the names of the
    cheeses can be found.
    """
    # Let's create a couple cheeses
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()
    # Create a request and then a response
    # for a list of cheeses
    request = rf.get(reverse('cheeses:list'))
    response = CheeseListView.as_view()(request)
    # Assert that the response contains both cheese names # in the template.
    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)

def test_cheese_create_form_valid(client, user):
    # Authenticate the user
    client.force_login(user)
    # Submit the cheese add form
    form_data = {
        "name": "Paski Sir",
        "description": "A salty hard cheese",
        "firmness": Cheese.Firmness.HARD, }
    url = reverse("cheeses:add")
    response = client.post(url, form_data)
    # Test the results for redirect
    assert response.status_code == 302 # Get the cheese based on the name
    cheese = Cheese.objects.get(name="Paski Sir")
    # Test that the cheese matches our form
    assert cheese.description == "A salty hard cheese"
    assert cheese.firmness == Cheese.Firmness.HARD
    assert cheese.creator == user
