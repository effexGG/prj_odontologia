from django.shortcuts import render, redirect
from .models import Personas
from .forms import PersonaForm

# Create your views here.

def index(request, template_name='odontologia/index.html'):
    return render(request, template_name)

def personas_listar(request, template_name='odontologia/personas.html'):
    personas = Personas.objects.all()
    dato_personas = {"personas": personas}
    return render(request, template_name, dato_personas)

def nuevo_paciente(request, template_name='odontologia/paciente_form.html'):
    if request.method =='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato = {"form":form}
    return render(request, template_name, dato)

def modificar_persona(request, pk, template_name='odontologia/paciente_form.html'):
    persona = Personas.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)

def eliminar_persona(request, pk,template_name='odontologia/confirmar_eliminar.html'):
    persona = Personas.objects.get(num_doc=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personas')
    else:
        dato = {'form':persona}
        return render(request, template_name, dato)
