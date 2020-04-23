from django import forms

class InputNumeroForm(forms.Form):
    numberOfTweets = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'input--style-5',
            'type': 'int',
            'name': 'numberOfTweets',

            
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input--style-5',
            'type':'text',
            'name':'username'
            
        }
    ))

    backGroundColor = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input--style-5',
            'type':'text',
            'name':'background',
            'value':'white'
            
        }
    ))