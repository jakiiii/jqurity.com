from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import FormMixin

from contact.forms import ContactForm

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
class PortfolioView(CreateView):
    form_class = ContactForm
    template_name = 'portfolio/portfolio.html'
    success_url = reverse_lazy('portfolio')

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

    def form_valid(self, form):
        instance = form.save(commit=True)
        print(instance)
        return super().form_valid(form)
