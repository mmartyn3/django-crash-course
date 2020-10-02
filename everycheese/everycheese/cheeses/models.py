from django.db import models

from django_countries.fields import CountryField
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Cheese(TimeStampedModel):
    """TimeStampedModel automatically gives the model 'created' and
    'modified' fields, which automatically track when the object is
    created or modified."""

    def __str__(self):
        return self.name

    class Firmness(models.TextChoices):
        """Note that we defined the firmness constants as variables within
        the scope of the Cheese model. This allows for direct comparisons."""
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi_soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField("Name of cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
        unique=True, always_update=False, populate_from="name")

    # Using the third party Django app django-countries to make a country
    # of origin field
    country_of_origin = CountryField('Country of origin', blank=True)

    # A good rule of thumb is to use TextField rather than CharField whenever
    # there might be a need for more than 255 characters.
    description = models.TextField("Description", blank=True)

    firmness = models.CharField("Firmness", max_length=20,
        choices=Firmness.choices, default=Firmness.UNSPECIFIED)
