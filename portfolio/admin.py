from django.contrib import admin

from .models import (
    SliderModel,
    AyatModel,
    ExperienceModel,
    FamiliarModel,
    InterestModel,
    PortfolioModel,
)


# Register your models here.
admin.site.register(SliderModel)
admin.site.register(AyatModel)
admin.site.register(ExperienceModel)
admin.site.register(FamiliarModel)
admin.site.register(InterestModel)
admin.site.register(PortfolioModel)
