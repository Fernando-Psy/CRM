from django import forms
from .models import Customer


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    firstName = forms.CharField(
        label='Nome',
        error_messages={'max_length': 'Nome não pode ter mais de 30 caracteres'}
    )
    lastName = forms.CharField(
        label='Sobrenome',
        error_messages={'max_length': 'Sobrenome não pode ter mais de 30 caracteres'}
    )
    email = forms.EmailField(label='Email')
    birthDate = forms.DateField(label='Data de nascimento', widget=DateInput())
    areaCode = forms.RegexField(
        label='DDD',
        regex=r'^\+?1?[0-9]{2}$',
        error_messages={'invalid': 'Número de DDD inválido'}
    )
    phoneNumber = forms.RegexField(
        label='Telefone',
        regex=r'^\+?1?[0-9]{9,15}$',
        error_messages={'invalid': 'Número de telefone inválido'}
    )
    country = forms.CharField(label='País')
    state = forms.CharField(label='Estado')
    city = forms.CharField(label='Cidade')

    class Meta:
        model = Customer
        fields = (
            'firstName',
            'lastName',
            'email',
            'birthDate',
            'areaCode',
            'phoneNumber',
            'country',
            'state',
            'city'
        )
