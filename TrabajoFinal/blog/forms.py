from django import forms


class AutorFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()
