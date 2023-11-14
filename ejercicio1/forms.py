from django import forms
import re

class Formulario(forms.Form):
    fechaInicio = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Fecha Inicio (dd/mm/YYYY)',
        help_text='Introduce la fecha de inicio'
    )

    fechaFin = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label= 'Fecha Fin (dd/mm/YYYY)',
        help_text= 'Introduce la fecha de fin')

    dias = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    diasSemana = forms.MultipleChoiceField(
        choices=dias,
        widget=forms.CheckboxSelectMultiple,
        label='Días de la semana',
        help_text='Selecciona un día de la semana' )

    correoElectronico = forms.CharField(
        label='Correo Electrónico',
        help_text='Introduce un correo perteneciente a iesmartinezm.es')

    def fechaMayor(self):
        fechaInicio = self.cleaned_data.get('fechaInicio')
        fechaFin = self.cleaned_data.get('fechaFin')

        if fechaInicio and fechaFin and fechaInicio > fechaFin:
            raise forms.ValidationError('La fecha de fin tiene que ser menor o igual a la fecha de inicio')

        return fechaInicio, fechaFin

    def clean_diasSemana(self):
        diasSemana = self.cleaned_data.get('diasSemana')

        if len(diasSemana) < 0:
            raise forms.ValidationError('Tienes que seleccionar al menos un día')

        if len(diasSemana) > 3:
            raise forms.ValidationError('Solo puedes seleccionar hasta 3 días')

        return diasSemana

    def clean_correoElectronico(self):
        correoElectronido = self.cleaned_data.get('correoElectronico')

        if not re.match(r'.*@iesmartinezm.es', correoElectronido):
            raise forms.ValidationError('El correo tiene que pertenecer a iesmartinezm.es')

        return correoElectronido

