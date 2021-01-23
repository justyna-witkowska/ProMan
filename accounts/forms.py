from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, BooleanField

from .models import Users


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'username']

    is_boss = BooleanField(label='Zaznacz tylko jeśli jesteś szefem')

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        is_boss = self.cleaned_data['is_boss']
        user = Users(is_boss=is_boss, user=result)
        if commit:
            user.save()
        return result
