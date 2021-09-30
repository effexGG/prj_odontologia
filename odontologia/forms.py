from django import forms
from django.forms import ModelForm
from .models import Localidad, Personas, Paciente, Usuario, Obrasocial, Calendario, Disponibilidad, Turno, Tratamiento, Prestacion,\
    Profesional, Piezadental, Establecimiento, Fichamedica, Fmedica_tratamiento
from dal import autocomplete

class DateInput(forms.DateInput):
    input_type = 'date'

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class PersonaForm(ModelForm):
    class Meta:
        model = Personas
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize',
                                                   'placeholder': 'Nombre Paciente'}),
                  'apellido':forms.TextInput(attrs={'class': 'form-control input', 'text-transform':'capitalize'}),
                  'num_doc':forms.TextInput(attrs={'type':'number', 'class':'form.control input'}),
                  'num_cuit': forms.TextInput(attrs={'type': 'number', 'class': 'form.control input'}),
                  'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input.sm'}),
                  'telefono': forms.TextInput(attrs={'class':'form-control input'}),
                  'email':forms.TextInput(attrs={'class':'form-control input'}),
                  'direccion':forms.TextInput(attrs={'class':'form-control input'}),
                 # 'localidad':forms.Select(attrs={'class':'form-control input'})
                  }


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {'paciente': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                   'placeholder': 'Nombre del paciente'}),
                   'num_hc': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                    'placeholder': 'Número de Historia Clínica'}),
                   'num_os': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                    'placeholder': 'Número de Obra Social'}),
                   'titular': forms.CheckboxInput(attrs={'is_checkbox': True})






        }



class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {'persona': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                  'placeholder': 'Persona'}),
                   'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                    'placeholder': 'Nombre de usuario'}),
                   'password': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                      'placeholder': 'Contraseña'})
                   }

class ObrasocialForm(ModelForm):
    class Meta:
        model = Obrasocial
        fields = '__all__'

class CalendarioForm(ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'

class DisponibilidadForm(ModelForm):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class PrestacionForm(ModelForm):
    class Meta:
        model = Prestacion
        fields = '__all__'

class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {'profesional': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                      'placeholder': 'Nombre del profesional'}),
                   'matricula': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                       'placeholder': 'Número de matrícula'}),
                   'especialidad': forms.TextInput(attrs={'class': 'form-control input',
                                                          'placeholder': 'Especialidad'}),
                   }

class PiezadentalForm(ModelForm):
    class Meta:
        model = Piezadental
        fields = '__all__'

class EstablecimientoForm(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'

class FichamedicaForm(ModelForm):
    class Meta:
        model = Fichamedica
        fields = '__all__'

class FmedicatratamientoForm(ModelForm):
    class Meta:
        model = Fmedica_tratamiento
        fields = '__all__'