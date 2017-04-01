'''
Crie um programa em python para cadastrar os dias da semana em um dicionário. Cada dia  da  semana  deverá  ser identificado por uma chave ordinal que  começará  em  1  (domingo)  e  finalizará  em  7  (sábado),  o valor deverá ser o nome  do  dia. Para  isso, defina duas  funções adicionarDia(posicao,dia) e exibirDias(dias)
'''

DiasDaSemana = {}

def adicionarDia(posicao, dia):
  if(posicao >= 1 and posicao <= 7):
        DiasDaSemana[posicao] = DiasDaSemana
        print(DiasDaSemana)
  else:
      print("A semana se inicia em 1  (domingo)  e  finaliza em  7  (sábado)! Por favor, digite um dia da semana válido!!!")
  return DiasDaSemana
  
def exibirDia():
  	for dia in DiasDaSemana:
  	  print("Dia: ", dia)
  	  print("")
    

def main():
    continuar = int(input("Digite (1) para adicionar mais um dia ou digite (2) para exibir os dias: \n"))
    if (continuar == 1):
      posicao = int(input("Informe a posição do dia: "))
      dia = str(input("Informe o dia: "))
      adicionarDia(posicao, dia)
    elif (continuar == 2):
      exibirDias(DiasDaSemana)
    else:
      print("Digite apenas (1) ou (2)")
      print("Digite (1) para adicionar mais um dia. \n Digite (2) para exibir os dias: \n")

if __name__ == "__main__":
    main()
