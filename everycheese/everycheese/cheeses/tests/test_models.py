import pytest

# connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Cheese


def test__str__():
    cheese = Cheese.objects.create(
        name="Brie",
        description = "soft French cheese",
        firmness = Cheese.Firmness.SOFT
    )
    assert cheese.__str__() == "Brie"
    assert str(cheese) == "Brie"
