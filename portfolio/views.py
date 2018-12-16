from django.shortcuts import render
from django.views.generic import DetailView


# Create your views here.
class PortfolioView(DetailView):
    template_name = 'portfolio/portfolio.html'

    def get_object(self, queryset=None):
        return self.request.user
