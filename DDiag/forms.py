from django import forms

class DiagnosisForm(forms.Form):
    no_preg = forms.IntegerField(help_text='Number of times pregnant', required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    glu = forms.IntegerField(help_text='Plasma glucose concentration', required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    bp = forms.IntegerField(help_text='Diastolic blood pressure', required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    st = forms.IntegerField(help_text='Triceps skin fold thickness \(mm\)', required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    isl = forms.IntegerField(help_text='2-hour serum insulin \(mu U\/ml\)', required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    bmi = forms.DecimalField(help_text='Body Mass Index \(weight in kg\/\(height in m\)^2\)', decimal_places=3, required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    dpf = forms.DecimalField(help_text='Diabetes pedigree function', decimal_places=3, required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
    age = forms.IntegerField(help_text='Age \(Minimum of 21 years\)', min_value=21, required=True, widget=forms.NumberInput(attrs={'style': "border:0px;border-bottom:1px solid #000;text-align:center"}))
