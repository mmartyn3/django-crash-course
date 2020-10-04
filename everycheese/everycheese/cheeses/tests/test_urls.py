import pytest

from django.urls import reverse, resolve

from .factories import CheeseFactory

# connect pytest to the database
pytestmark = pytest.mark.django_db

# These tests will prevent 404 errors

# since we'll need an instanciated cheese object multiple times during tests,
# we will make one here and call on that
@pytest.fixture
def cheese():
    return CheeseFactory()

#####################################
# Test the Cheese List URL Patterns #
#####################################

def test_list_reverse():
    """cheeses:list should reverse to /cheeses/.
    Reversing the view name should give us the absolute URL."""
    assert reverse('cheeses:list') == '/cheeses/'

def test_list_resolve():
    """/cheeses/ should resolve to cheeses:list.
    Resolving the absolute URL should give us the view name."""
    assert resolve('/cheeses/').view_name == 'cheeses:list'

####################################
# Test the Add Cheese URL Patterns #
####################################

def test_add_reverse():
    """cheeses:add should reverse to /cheeses/add/."""
    assert reverse('cheeses:add') == '/cheeses/add/'

def test_add_resolve():
    """/cheeses/add/ should resolve to cheeses:add."""
    assert resolve('/cheeses/add/').view_name == 'cheeses:add'

########################################
# Test the Cheese Deatail URL Patterns #
########################################

def test_detail_reverse(cheese):
    """cheeses:detail should reverse to /cheeses/cheeseslug/."""
    url = reverse('cheeses:detail',
        kwargs={'slug': cheese.slug})
    assert url == f'/cheeses/{cheese.slug}/'

def test_detail_resolve(cheese):
    """/cheeses/cheeseslug/ should resolve to cheeses:detail."""
    url = f'/cheeses/{cheese.slug}/'
    assert resolve(url).view_name == 'cheeses:detail'
