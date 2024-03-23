from django import forms
from .models import Laptop


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'


        widgets = {
            "var_name": forms.TextInput(attrs={'class': 'form-control'}),
            " year_of_manufact": forms.NumberInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "outlet": forms.Select(attrs={'class': 'form-control'}),
        }
