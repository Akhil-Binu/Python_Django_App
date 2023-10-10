from django.contrib import admin

# Register your models here.
from .models import Departments

from .models import Doctors

admin.site.register(Departments)
admin.site.register(Doctors)