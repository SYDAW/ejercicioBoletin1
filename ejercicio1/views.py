from django.shortcuts import render
from .forms import Formulario

def crearFormulario(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            fechaInicio = form.cleaned_data['fechaInicio']
            fechaFin = form.cleaned_data['fechaFin']
            diasSemana = form.cleaned_data['diasSemana']
            correoElectronico = form.cleaned_data['correoElectronico']

            return render(request, 'ejercicio1/todoBien.html', {})

        else:
            mensaje_error = "No has hecho bien algo"
            return render(request, 'ejercicio1/crearFormulario.html', {'form': form, 'mensaje_error': mensaje_error})

    else:
        form = Formulario()

    return render(request, 'ejercicio1/crearFormulario.html', {'form': form})




