from django import forms

class SearchForm(forms.Form):
	search_word = forms.CharField(label="Search",widget=forms.TextInput(),max_length=100,required=False)