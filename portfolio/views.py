from django.shortcuts import render
from django.views.generic import DetailView

from .models import (
    Slider,
    Ayat,
    Experience,
    Familiar,
    Interest,
    Portfolio
)
from about.models import (
    AboutModel,
    SocialModel
)


# Create your views here.
class PortfolioView(DetailView):
    template_name = 'portfolio/portfolio.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Portfolio'
        context['slider_info'] = Slider.objects.all()[:1]
        context['al_Quran_verse'] = Ayat.objects.all()[:1]
        context['about_info'] = AboutModel.objects.all()[:1]
        context['social_link'] = SocialModel.objects.all()[:1]
        context['experience_info'] = Experience.objects.all()
        context['familiar_info'] = Familiar.objects.all()
        context['interest_info'] = Interest.objects.all()
        context['portfolio_info'] = Portfolio.objects.all()[:8]
        return context
