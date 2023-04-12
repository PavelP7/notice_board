from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2",
        )

    def __init__(self, *args, **kwargs):
        super(BaseRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in list(self.fields):
            self.fields[fieldname].help_text = None
