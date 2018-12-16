from django.contrib import admin

from .models import (
    Slider,
    Ayat,
    Experience,
    Familiar,
    Interest,
    Portfolio,
)


# Register your models here.
admin.site.register(Slider)
admin.site.register(Ayat)
admin.site.register(Experience)
admin.site.register(Familiar)
admin.site.register(Interest)
admin.site.register(Portfolio)
