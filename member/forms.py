from django import forms
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from .models import Profile


class SignupForm(forms.Form):
    first_name = forms.CharField(label=_('First name'),
                                 max_length=30,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                _('First name'), }))
    last_name = forms.CharField(label=_('Last name'),
                                max_length=30,
                                widget=forms.TextInput(
                                    attrs={'placeholder':
                                               _('Last name'), }))
    phone = forms.CharField(label=_('Phone number'),
                            max_length=30,
                            widget=forms.TextInput(
                                attrs={'placeholder':
                                           _('Phone number'), }))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile()
        profile.user = user
        profile.phone = self.cleaned_data['phone']
        profile.save()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']