from django import forms
from django.contrib.auth.models import User

# This form will be used to authenticate users against the database. Note that you use the PasswordInput
# widget to render the password HTML element. This will include type="password" in the HTML so
# that the browser treats it as a password input.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    # The clean_password2 method checks that the two passwords provided by the user match. If they don't, a ValidationError is raised.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']