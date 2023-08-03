from django import forms

from catalog.models import Product

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                   'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        for word in forbidden_words:

            if word in cleaned_data.lower():
                raise forms.ValidationError('Нельзя использовать такое название!')
        return cleaned_data

    def clean_product_description(self):

        cleaned_data = self.cleaned_data['product_description']

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Нельзя использовать такое описпание!')
        return cleaned_data
