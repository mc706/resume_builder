from django import forms
from resumes.models import Resume, Section, Entry


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = (
            'title',
            'name',
            'address1',
            'address2',
            'csz',
            'email',
            'phone',
        )


class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = (
            'section_type',
            'title',
        )


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = (
            'title',
            'subtitle',
            'date_start',
            'date_finish',
            'description',
        )