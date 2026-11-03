from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'ordform'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'ordform'}))
    product = forms.ChoiceField(choices=(('5000000','Laptop'),('3000000','Smartphone'),('200000','Headphones'),),widget=forms.Select(attrs={'class':'ordform'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'ordform'}))
    delivery = forms.ChoiceField(choices=(('0','PickUp - Free'),('30000',"Courier")),widget=forms.Select(attrs={'class':'ordform'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'ordform'}))