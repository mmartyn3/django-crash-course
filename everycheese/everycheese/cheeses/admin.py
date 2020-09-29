from django.contrib import admin
from .models import Cheese

# registering the Cheese Model to Admin
admin.site.register(Cheese)
