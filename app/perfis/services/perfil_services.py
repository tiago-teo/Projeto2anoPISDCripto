from ..models import Perfil


def listar_perfil():
    perfis = Perfil.objects.all()
    return perfis


def listar_perfil_id(id):
    perfil = Perfil.objects.get(id=id)
    return perfil


def remover_perfil(perfil):
    perfil.delete()


def cadastrar_perfil(perfil):
    Perfil.objects.create(nome=perfil.nome, foto=perfil.foto, curriculo=perfil.curriculo)


def editar_perfil(perfil, perfil_novo):
    perfil.nome = perfil_novo.nome
    perfil.foto = perfil_novo.foto
    perfil.curriculo = perfil_novo.curriculo
    perfil.save(force_update=True)
