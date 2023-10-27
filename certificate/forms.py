from django import forms


class TokenForm(forms.Form):
    token = forms.CharField(
        label="Token",
        max_length=1000,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter token here...',
        })
    )
