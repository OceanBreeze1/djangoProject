from django.forms import ModelForm
from apps.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ()
