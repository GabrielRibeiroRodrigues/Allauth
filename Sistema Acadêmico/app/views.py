# app/views.py
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'app/index.html')

def notas(request):
    form = Nota()
    return render(request, 'app/area_aluno.html', {'form': form})

def logar(request):
    if request.method == "GET":
        return render(request, 'app/login.html', )
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login(request, user)
            return HttpResponse("Autenticado")
        else:
            return HttpResponse("Nome ou senha inválidos")
@login_required(login_url="/login")
def plataforma(request):
    return HttpResponse("Logado")
def cadastro(request):
    if request.method == "GET":
        return render(request, 'app/cadastro.html',)
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username = username, email = email, password = senha, is_staff = False)
        user.save()
        return HttpResponse("Usuario Cadastrado")

def pessoas(request):
    pessoas = Pessoa.objects.all() 
    context = {'pessoas': pessoas}
    return render(request, 'app/pessoas.html',context)


def ensino(request):
    ensino = InstituicaoEnsino.objects.all() 
    context = {'ensino': ensino}
    return render(request, 'app/ensino.html',context)


def areas(request):
    areas = AreaSaber.objects.all()  
    return render(request, 'app/areas.html', {'areas': areas})


def cursos(request):
    cursos = Curso.objects.all() 
    context = {'cursos': cursos}
    return render(request, 'app/cursos.html',context)


def disciplina(request):
    disciplina = Disciplina.objects.all() 
    context = {'disciplinas': disciplina}   
    return render(request, 'app/disciplina.html',context)


def matriculas(request):
    matriculas = Matricula.objects.all() 
    context = {'matriculas': matriculas}
    return render(request, 'app/matriculas.html',context)


def avaliacoes(request):
    avaliacoes = Avaliacao.objects.all() 
    context = {'avaliacoes': avaliacoes}
    return render(request, 'app/avaliacoes.html',context)  


def frequencias(request):
    frequencias = Frequencia.objects.all() 
    context = {'frequencias': frequencias}
    return render(request, 'app/frequencias.html',context)  

def turmas(request):
    turmas = Turma.objects.all() 
    context = {'turmas': turmas}
    return render(request, 'app/turmas.html',context)  

def cidades(request):
    cidades = Cidade.objects.all() 
    context = {'cidades': cidades}
    return render(request, 'app/cidades.html',context)  


def ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all() 
    context = {'ocorrencias': ocorrencias}
    return render(request, 'app/ocorrencias.html',context)


def disciplinas_cursos(request):
    disciplinas_cursos = DisciplinaPorCurso.objects.all() 
    context = {'disciplinas_cursos': disciplinas_cursos}
    return render(request, 'app/disciplinas_cursos.html',context)

def tipos_avaliacao(request):
    tipos_avaliacao = TipoAvaliacao.objects.all() 
    context = {'tipos_avaliacao': tipos_avaliacao}
    return render(request, 'app/tipos_avaliacao.html',context)

def disciplinas_cursos(request):
    disciplinas_cursos = DisciplinaPorCurso.objects.select_related('disciplina', 'curso', 'periodo').all()
    context = {'disciplinas_cursos': disciplinas_cursos}
    return render(request, 'app/disciplinas_cursos.html', context)