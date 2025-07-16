from django import forms

class PatientForm(forms.Form):
    age = forms.IntegerField(label='Age')
    cholesterol = forms.FloatField(label='Cholesterol')
    blood_pressure = forms.FloatField(label='Blood Pressure')
    max_heart_rate = forms.FloatField(label='Max Heart Rate')
