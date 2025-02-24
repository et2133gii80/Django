from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    forbidden_words  = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['status', 'owner']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['img'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите изображение'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену'
        })

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if product_name.lower() in self.forbidden_words:
            raise ValidationError('запрещенное слово')
        return product_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description.lower() in self.forbidden_words:
            raise ValidationError('запрещенное слово')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('цена некорректная')
        return price

class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].widget.attrs.update({
            'class': 'form-check-input',
            'placeholder': 'Укажите статус товара'
        })




