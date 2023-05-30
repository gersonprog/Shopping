from django import forms
from Site.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        



# from django import from .forms import
# from Site.models import Cliente
