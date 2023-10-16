from django import forms


class TokenForm(forms.Form):
    token = forms.CharField(
        label="Token",
        max_length=1000,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Add the 'form-control' class for Bootstrap styling
            'placeholder': 'Enter token here...',  # Add a placeholder text
        })
    )
