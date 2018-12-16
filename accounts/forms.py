from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.messages.views import messages

from .signals import user_logged_in

User = get_user_model()


# Create your form here.
class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=32, label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password have to match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'admin'
        )

    def clean_password(self):
        return self.initial["password"]


class UserInfoChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=120, label='First Name', required=False)
    last_name = forms.CharField(max_length=120, label='Last Name', required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')
        qs = User.objects.filter(email=email)
        if qs.exists():
            not_active = qs.filter(is_active=False)
            if not_active.exists():
                msg = messages.error(self.request, "This user is not active!")
                raise forms.ValidationError(msg)
        user = authenticate(self.request, email=email, password=password)
        if user is None:
            msg = messages.error(self.request, "Invalid credentials.")
            raise forms.ValidationError(msg)
        login(self.request, user)
        user_logged_in.send(user.__class__, instance=user, request=self.request)
        return data
