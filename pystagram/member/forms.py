from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # class_default_fields = ('password1', 'password2')

        for field in ('password1', 'password2'):
            if field == 'password1':
                self.fields[field].label = '비밀번호'
            else:
                self.fields[field].label = '비밀번호 확인'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')
        labels = {
            'email': '이메일',
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'example@example.com'
                }
            )
        }
