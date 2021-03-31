from django import forms
from django.forms import ModelForm
from . import models

code = "Kode Barang"
product_name = "Nama Barang"
unit_name = "Nama Satuan"
base_price = "Harga Dasar"
base_stock = "Stok Awal"
unit = "Satuan"

class form_add_product(ModelForm):
    class Meta:
        model = models.Products
        exclude = ('user',) 
        labels = {
            "code": code,
            "name": product_name,
            "base_price": base_price,
            "base_stock": base_stock,
            "unit": unit,
        }
        


class form_add_unit(ModelForm):
    class Meta:
        model = models.Units
        exclude = ('user',)
        labels = {
            "name": unit_name,
        }
