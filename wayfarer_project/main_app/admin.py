from django.contrib import admin

from .models import Profile, TravelPost

from .models import Profile, TravelPost, City

# Register your models here.
admin.site.register(Profile)
admin.site.register(TravelPost)


admin.site.register(City)

