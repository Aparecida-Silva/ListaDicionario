turmas = {}

def calcularMedia(nota1, nota2):
  matricula = [nota1, nota2]
  media = (nota1 + nota2) / 2
  print("A média é: ",media)

def adicionarTurma(turma):
  turmas[turma] = {}

def adicionarAlunoNotas (turma, matricula, nota1, nota2):
  turmas[turma][matricula] = [nota1,nota2]
  
def ResultadoFinal():
  print(turmas)
  
def main(Args=None):
  print("")
  print("(1) Adicionar turma")
  print("(2) Adicionar aluno e notas")
  print("(3) Calcular média de um Aluno")
  print("(4) Exibir todas as turmas e seus alunos")
  print("(5) sair")
  alternativa = int(input("Escolha uma das alternativas que foram propostas acima: "))
  print("")
  if(alternativa == 1):
    QuantTurmas = int(input("Digite uma determinada quantidade de turmas que você deseja adicionar: "))
    for x in range (0, QuantTurmas):
      turma = eval(input("Digite uma identificação para a turma (ex: 1BINFO): "))
      adicionarTurma(turma)

  if(alternativa == 2):
    turma = eval(input("Digite qual é a turma que você deseja adicionar o aluno: "))
    if (turma in turmas):
      matricula = int(input("Digite a matrícula do aluno: "))
      global notas
      nota1 = eval(input("Digite a primeira nota:"))
      nota2 = eval(input("Digite a segunda nota:"))
      adicionarAlunoNotas(turma, matricula, nota1, nota2)
    
  if(alternativa == 3):
    turma = int(input("Digite a turma do aluno: "))
    matricula = int(input("Digite a matrícula do aluno: "))
    calcularMedia(turmas[turma][matricula][0], turmas[turma][matricula][1])
    
  if (alternativa == 4):
    ResultFinal()
    
  if (alternativa == 5):
    print("Programa finalizado!")
  else:
    print("Opção de número inválido!")
if (__name__ == "__main__"):
    main()
