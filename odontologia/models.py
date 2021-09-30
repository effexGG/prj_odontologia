from django.db import models
from datetime import datetime


DIA_CHOICE =(
    (1, "Lunes"),
    (2, "Martes"),
    (3, "Miercoles"),
    (4, "Jueves"),
    (5, "Viernes"),
    (6,"Sabado"),
    (0,"Domingo")


)
# Create your models here.
class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField("Codigo Postal")

    class Meta:
        verbose_name_plural = 'Localidades'


    def __str__(self):
        return self.nombre


class Personas(models.Model):
    num_doc = models.IntegerField("Numero Documento", primary_key=True)
    nombre = models.CharField("Nombres", max_length=150)
    apellido = models.CharField("Apellido", max_length=150)
    num_cuit = models.CharField("Numero Cuit/Cuil",max_length=15,null=True,blank=True)
    fecha_nac = models.DateField("Fecha Nacimiento", default=datetime.now)
    telefono = models.CharField("Numero Telefono", max_length=50, null=True, blank=True)
    email = models.EmailField ("E-mail", null=True, blank=True)
    direccion = models.CharField("Domicilio", max_length=150)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="persona_localidad")

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name_plural = 'Personas'

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)


class Usuario(models.Model):
    persona = models.ForeignKey(Personas, on_delete=models.PROTECT, related_name="usuario_persona")
    nombre = models.CharField("Nombre", max_length=150, primary_key=True)
    password = models.CharField("Contraseña", max_length=15)

    def __str__(self):
        return self.nombre

class Obrasocial(models.Model):
    nombre_os = models.CharField("Nombre Obra Social",max_length=150, primary_key=True)
    direccion = models.CharField("Domicilio",max_length= 50)
    disponibilidad = models.BooleanField("Disponible")

    def __str__(self):
        return self.nombre_os


class Calendario(models.Model):
    dia = models.CharField ("Dia de la semana", max_length=1, choices=DIA_CHOICE, default=1)
    hora = models.DateTimeField

class Paciente(models.Model):
    paciente = models.ForeignKey(Personas, on_delete=models.PROTECT, related_name="paciente_persona")
    num_hc = models.IntegerField("Numero de Historia Clinica", primary_key=True)
    obra_social = models.ForeignKey(Obrasocial, on_delete=models.PROTECT, related_name="paciente_obrasocial")
    num_os = models.CharField("Nunero Obra Social", max_length=150)
    titular_familiar = models.CharField("Titular Obra Social", max_length=100, null=True , blank=True)

    class Meta:
        ordering = ["paciente", "num_hc"]

    def __str__(self):
        return self.paciente


class Profesional(models.Model):
    profesional = models.ForeignKey(Personas, on_delete=models.PROTECT, related_name="profesional_persona")
    matricula = models.IntegerField("Numero de Matricula ", primary_key=True)
    especialidad = models.CharField("Especialidad ", max_length=50)

class Disponibilidad(models.Model):
    profesional = models.ForeignKey (Profesional, on_delete=models.PROTECT, related_name="disponibilidad_profesional")
    dia_hora = models.ForeignKey(Calendario, on_delete=models.PROTECT, related_name="disponibilidad_calendario")

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="turno_paciente")
    medico = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name="turno_profesional")
    fecha = models.DateField("Fecha Turno", default=datetime)
    estado = models.CharField("Estado del turno", max_length=50)

    class Meta:
        verbose_name_plural = 'Turnos'

    def _str_(self):
        return '%s, %s, %s' % (self.paciente, self.medico, self.fecha)

class Establecimiento(models.Model):
    nombre = models.CharField("Nombre del establecimiento", max_length=150)
    razon_social = models.CharField("Razon social del establecimiento", max_length=30)
    direccion = models.CharField("Domicilio establecimiento", max_length=150)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="establecimiento_localidad")
    telefono = models.CharField("Numero de telefono", max_length=30)
    email = models.CharField("Email del establecimiento", max_length=150, null=True, blank=True)
    web = models.CharField("Web del establecimiento", max_length=150)

class Piezadental(models.Model):
    nombre = models.CharField("Nombre pieza dental", max_length=50)

    class Meta:
        verbose_name_plural = 'Piezas dentales'

    def _str_(self):
        return self.nombre


class Prestacion(models.Model):
    nombre = models.CharField("Nombre tipo de prestacion", max_length=50)
    descripcion = models.CharField("Detalle del Trabajo realizadoo", max_length=150)
    pieza_dental= models.ForeignKey(Piezadental, on_delete=models.PROTECT, related_name="prestacion_piezadental")

    class Meta:
        verbose_name_plural = 'Prestaciones'

    def _str_(self):
        return '%s, %s, %s' % (self.nombre, self.descripcion, self.pieza_dental)

class Fichamedica(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT, related_name="fichamedica_establecimiento")
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="fichamedica_paciente")
    fecha_alta = models.DateField("Fecha alta ", default=datetime)
    tipo_sangre = models.CharField("Tipo grupo sanguineo", max_length=10)
    antecedentes = models.CharField("Anteriores consultas", max_length=150, null=True, blank=True)
    medicacion = models.CharField("Prescripciones farmacologicas", max_length=150, null=True, blank=True)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name="fichamedica_prestacion")

class Tratamiento(models.Model):
    medico_efector = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name="tratamiento_profesional")
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name="tratamiento_prestacion")
    fecha = models.DateField("Fecha prestacion", default=datetime)
    observacion = models.CharField("Observaciones:", max_length=150,  null=True, blank=True)

class Fmedica_tratamiento(models.Model):
    fichamedica = models.ForeignKey(Fichamedica, on_delete=models.PROTECT, related_name="fmtratamiento_fichamedica")
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.PROTECT, related_name="fmtratamiento_tratamiento")
