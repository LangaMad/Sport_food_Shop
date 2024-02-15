from django import forms



class CartForm(forms.Form):
    quantity = forms.IntegerField(
        label='Quantity',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Quantity',
            }
        )
    )
    update = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput()
    )




