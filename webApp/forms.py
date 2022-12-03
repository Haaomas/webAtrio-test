from .models import Person
from django import forms


class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'birth_date']
        labels = {'firstname': 'Prénom', 'lastname': 'Nom',
                  'birth_date': 'Date de naissance'}
