from django.contrib import admin
from .models import (
    Employee,
    Language,
    Department
)

admin.site.register(Employee)
admin.site.register(Language)
admin.site.register(Department)
