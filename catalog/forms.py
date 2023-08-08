from django import forms

from catalog.models import Product, Version

# Запрещенные слова для регистрации товара
forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                   'радар']


class StyleFormMixin:
    """
    Стиль для отображения формы заполнения
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания и изменения продукта
    """
    class Meta:
        model = Product
        exclude = ('user',)

    def clean_product_name(self):
        """
        Проверка на наличие запрещенных слов в названии
        """
        cleaned_data = self.cleaned_data['product_name']

        for word in forbidden_words:

            if word in cleaned_data.lower():
                raise forms.ValidationError('Нельзя использовать такое название!')
        return cleaned_data

    def clean_product_description(self):
        """
        Проверка на наличие запрещенных слов в описание
        """

        cleaned_data = self.cleaned_data['product_description']

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Нельзя использовать такое описпание!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания и изменения версий продукта
    """
    class Meta:
        model = Version
        fields = '__all__'
