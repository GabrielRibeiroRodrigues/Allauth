from django.urls import path,include
from .import views 
urlpatterns = [
     path('', views.index, name='index'),
        path('areas/', views.areas, name = 'areas'),
         path('avaliacoes/', views.avaliacoes, name = 'avaliacoes'),
         path('cidades/', views.cidades, name = 'cidades'),
         path('cursos/', views.cursos, name = 'cursos'),
         path('disciplinas_cursos/', views.disciplinas_cursos, name = 'disciplinas_cursos'),
         path('disciplina/', views.disciplina, name = 'disciplina'),
         path('ensino/', views.ensino, name = 'ensino'),
         path('frequencias/', views.frequencias, name = 'frequencias'),
         path('matriculas/', views.matriculas, name = 'matriculas'),
         path('ocorrencias/', views.ocorrencias, name = 'ocorrencias'),
         path('pessoas/', views.pessoas, name = 'pessoas'),
         path('tipos_avaliacao/', views.tipos_avaliacao, name = 'tipos_avaliacao'),
         path('turmas/', views.turmas, name = 'turmas'),
         path('area_aluno/', views.notas, name = 'area_aluno'),
         path('login/', views.logar, name = 'login'),
         path('cadastro/', views.cadastro, name = 'cadastro'),
         path('plataforma/', views.plataforma, name = 'plataforma ' )
         
         
]
