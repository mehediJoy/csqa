from allauth.account.forms import LoginForm, SignupForm
from django import forms

class NewLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(NewLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'input'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input'})
        
class NewSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(NewSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'input'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input'})
        