from django.contrib.auth.forms import UserCreationForm

from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email address'









