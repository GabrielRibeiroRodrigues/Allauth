from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_do_pai = models.CharField(max_length=100)
    nome_da_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey('Cidade', on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.ForeignKey('Ocupacao', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey('Cidade', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey('AreaSaber', on_delete=models.SET_NULL, null=True, blank=True)
    instituicao = models.ForeignKey('InstituicaoEnsino', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class PeriodoCurso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey('AreaSaber', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    instituicao = models.ForeignKey('InstituicaoEnsino', on_delete=models.SET_NULL, null=True, blank=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

class Avaliacao(models.Model):
    descricao = models.TextField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Frequencia(models.Model):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True, blank=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, null=True, blank=True)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, null=True, blank=True)



class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class DisciplinaPorCurso(models.Model):
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    periodo = models.ForeignKey('PeriodoCurso', on_delete=models.CASCADE)
