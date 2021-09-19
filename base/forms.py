from django import forms

class allocateform(forms.Form):
    client = forms.CharField(label='client', widget=forms.TextInput(attrs={'id': 'search', 'placeholder': 'Client','autocomplete':"off"}))
    type = forms.CharField(max_length = 15)
    weight = forms.IntegerField()