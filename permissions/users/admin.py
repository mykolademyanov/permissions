from django.contrib import admin
from users.models import User, Role


admin.site.register(User)
admin.site.register(Role)
