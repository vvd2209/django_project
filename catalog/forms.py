from django import forms

from catalog.constants import forbidden_words
from catalog.models import Product, Version


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_active":
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете неразрешенное слово "{forbidden_word.title()}". '
                                            f'Повторите ввод.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете неразрешенное слово "{forbidden_word.title()}" '
                                            f'Повторите ввод.')

        return cleaned_data

class ProductFormModerator(StyleForMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                       'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_active',)

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете неразрешенное слово "{forbidden_word.title()}" '
                                            f'Повторите ввод.')

        return cleaned_data

class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
