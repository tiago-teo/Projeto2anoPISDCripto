from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfil
from .forms import PerfilForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#View que cria uma instância do formulário para atualizar o perfil com a PK(Primary Key) fornecida. O Perfil é criado automaticamente com o registo de utilizador
def perfil_update(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            for field in form.fields:
                if not form.cleaned_data.get(field):
                    form.cleaned_data[field] = getattr(perfil, field)
            form.save()
            user = get_object_or_404(User, pk=pk)
            user.username = perfil.nome
            user.save()
            messages.success(request, 'Your profile is updated successfully')
            form = PerfilForm()
            return render(request, 'perfil_form.html', {'form': form, 'perfil': perfil})
    else:
        perfis = Perfil.objects.all()
        form = PerfilForm()
    return render(request, 'perfil_form.html', {'form': form, 'perfil': perfil})


