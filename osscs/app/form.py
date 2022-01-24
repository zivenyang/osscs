from django import forms


class SearchForm(forms.Form):
    REPOSITORY_TYPE_CHOICES = (
        (0, 'MAVEN'),
        (1, 'PYPI')
    )
    repository_type = forms.ChoiceField(label='开源软件类型', choices=REPOSITORY_TYPE_CHOICES)
    query = forms.CharField(label='查询', max_length=50)
