from django import forms

class Nota(forms.Form):
    nota1 = forms.IntegerField()
    nota2 = forms.IntegerField()
    nota3 = forms.IntegerField()
