from django import forms

class CalcForm(forms.Form):
    first_num = forms.FloatField(widget=forms. NumberInput(attrs={'class':'calcform'}))
    second_num = forms.FloatField(widget=forms.NumberInput(attrs={'class':'calcform'}))
    operation = forms.ChoiceField(choices=(('+', "Сложение"), ('-', "Вычитание"), ('x', "Умножение"),('÷',"Деление")))
