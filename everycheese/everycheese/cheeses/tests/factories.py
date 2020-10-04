from django.template.defaultfilters import slugify
from everycheese.users.tests.factories import UserFactory

import factory
import factory.fuzzy

from ..models import Cheese

import pytest


@pytest.fixture
def cheese():
    return CheeseFactory()

class CheeseFactory(factory.django.DjangoModelFactory):
    """Autogenerates Cheese objects (model instances)."""

    # Autogenerate a name using FuzzyText
    name=factory.fuzzy.FuzzyText()

    # slugify the randomly choosen name from above
    slug=factory.LazyAttribute(lambda obj: slugify(obj.name))

    # randomly generate a description as a paragraph
    description=factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )

    country_of_origin = factory.Faker('country_code')

    creator = factory.SubFactory(UserFactory)

    # randomly select a firmness from the list of options in cheeses/models.py
    firmness=factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])

    class Meta:
        model = Cheese



"""
How to call the CheeseFactory Class in order to create 10 fake cheeses to test the UI

python manage.py shell_plus

In [1]: from everycheese.cheeses.tests.factories import CheeseFactory

In [2]: for i in range(10):
   ...:     CheeseFactory(name=f"Fake cheese {i}")

In [3]: Cheese.objects.all() # this will display all cheeses in the DB (or exit and head to /admin)

In [4]: Cheese.objects.filter(name__startswith='Fake').delete() # delete all fake cheeses
"""
