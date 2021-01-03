from django import forms

class todoListForm(forms.Form):
    text = forms.CharField(max_length = 45,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter to do','aria-label':'Todo','aria-describeby':'add-btn'}))