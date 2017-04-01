'''
Crie  um  programa  em  python  para  cadastrar os funcionários  de  uma empresa.  Cada  funcionário é  identificado  por  sua  matrícula  e nome. Para  isso, defina três funções  adicionarFuncionario(matricula,nome), buscarFuncionario(matricula)e exibirFuncionarios(funcionarios)
'''

Funcionarios = {}

def adicionarFuncionario(matricula, nome):
  Funcionarios[matricula] = nome
  print(Funcionarios)
  return Funcionarios
    
def buscarFuncionario(matricula):
  matricula = int(input("Digite a matricula do funcionário para buscar: "))
  if matricula in Funcionarios:
    print("Funcionário: ", Funcionários[matricula])
  else:
    print("Esta matricula que você digitou ainda não se encontra na lista de funcionários cadastrados!")
        
def exibirFuncionario(Funcionarios):
    for X in Funcionarios:
        print("Funcionário: ", X)
        print("")
        
def main(Args=None):
    continuar = ("sim")
    while (continuar == "sim"):
        print("")
        print("(1) Adicionar funcionário")
        print("(2 )Buscar funcionário")
        print("(3) Exibir funcionários")
        print("(4) Sair")
        alternativa = int(input("Escolha uma das alternativas que foram propostas acima: "))
        print("")
        if (alternativa == 1):
            matricula = int(input("Digite a matrícula do funcionário: "))
            nome = str(input("Digite o nome do funcionário: "))
            adicionarFuncionario(matricula, nome)
        elif (alternativa == 2):
            matricula = int(input("Digite a matrícula do funcionário: "))
            buscarFuncionario(matricula)
        elif (alternativa == 3):
            exibirFuncionario(Funcionarios)
        elif (alternativa == 4):
            continuar = ("não")
            print("Programa Finalizado!")
        else:
            print("Número escolhido inválido")
if(__name__ == __name__):
