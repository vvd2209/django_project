from django import forms

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
        fields = '__all__'
        # fields = ('name', 'description', 'image',)
        # fields = ('name', 'image', 'category', 'price',)
        # exclude = ('is_active',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете неразрешенное слово "{forbidden_word.title()}". '
                                            f'Повторите ввод.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете неразрешенное слово "{forbidden_word.title()}" '
                                            f'Повторите ввод.')

        return cleaned_data


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
