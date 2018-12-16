from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView, View
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe
from django.contrib.messages.views import SuccessMessageMixin, messages

from .forms import UserLoginForm


# Create your views here.
class RequestFormAttachMixin(object):
    def get_form_kwargs(self):
        kwargs = super(RequestFormAttachMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class NextUrlMixin(object):
    default_next = '/'

    def get_next_url(self):
        next_ = self.request.GET.get('next')
        next_post = self.request.POST.get('next')
        redirect_path = next_ or next_post or None
        if is_safe_url(redirect_path, self.request.get_host()):
            return redirect_path
        return self.default_next


class UserLoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = UserLoginForm
    success_url = '/profile/'
    default_next = '/profile/'
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


def get_logout(request):
    logout(request)
    return redirect('home')
