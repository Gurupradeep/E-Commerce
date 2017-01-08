from django import forms

class BotForm(forms.Form):
    search_text = forms.CharField(max_length=100)