from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'stform'}))
    surename = forms.CharField(widget=forms.TextInput(attrs={'class':'stform'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'stform'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'stform'}))