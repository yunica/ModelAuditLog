from django.shortcuts import render
from Base.models import FirstModel
from audit.auditor import Audit
from audit.models import Auditor


# Create your views here.
def listar(request):
    return render(request, 'inicio.html', {'aud': Auditor.objects.all()})


# Create your views here.
def agregar(request):
    nf = FirstModel(name='primero', text='primer texto', user=request.user)
    nf.save()
    auditor = Audit(request, nf)
    auditor.create()

    return render(request, 'inicio.html', {'aud': []})


def modificar(request):
    nf = FirstModel.objects.first()
    auditor = Audit(request, nf)
    nf.name = 'segundo 11'
    nf.text = 'segundo texto 11'
    nf.save()
    auditor.update()

    return render(request, 'inicio.html', {'aud': Auditor.objects.all()})
