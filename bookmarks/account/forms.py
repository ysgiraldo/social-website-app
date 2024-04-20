from django import forms

# This form will be used to authenticate users against the database. Note that you use the PasswordInput
# widget to render the password HTML element. This will include type="password" in the HTML so
# that the browser treats it as a password input.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)