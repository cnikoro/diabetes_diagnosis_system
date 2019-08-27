from django import forms

class DiagnosisForm(forms.Form):
    no_preg = forms.IntegerField(help_text='Number of times pregnant', required=True)
    glu = forms.IntegerField(help_text='Plasma glucose concentration', required=True)
    bp = forms.IntegerField(help_text='Diastolic blood pressure', required=True)
    st = forms.IntegerField(help_text='Triceps skin fold thickness \(mm\)', required=True)
    isl = forms.IntegerField(help_text='2-hour serum insulin \(mu U\/ml\)', required=True)
    bmi = forms.DecimalField(help_text='Body Mass Index \(weight in kg\/\(height in m\)^2\)', decimal_places=3, required=True)
    dpf = forms.DecimalField(help_text='Diabetes pedigree function', decimal_places=3, required=True)
    age = forms.IntegerField(help_text='Age \(Minimum of 21 years\)', min_value=21, required=True)
