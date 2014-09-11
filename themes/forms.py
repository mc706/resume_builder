from django import forms
from themes.models import Template, Style


class TemplateForm(forms.ModelForm):

    class Meta:
        model = Template
        fields = (
            'name',
            'global_styles',
        )


class StyleForm(forms.ModelForm):

    class Meta:
        model = Style
        fields = (
            'section',
            'style',
        )