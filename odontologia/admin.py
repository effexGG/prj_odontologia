from django.contrib import admin
from  .models import *

# Register your models here.

my_models = [Localidad, Personas]

admin.site.register(my_models)
