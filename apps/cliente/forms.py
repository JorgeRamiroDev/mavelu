from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']