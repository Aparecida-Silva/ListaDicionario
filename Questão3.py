'''
Um supermercado necessita gerenciar através  de  software os preços dos produtos que são oferecidos nas gondolas. Cada produto é definido como um item descrito por seu nome(chave) e preço(valor). Baseado nessas informações crie um programa que atenda esses requisitos:
a. Cadastrar o  produto  e seu preço. Defina uma função chamada cadastrarProduto(produtos,produto,   preco) para adicionar o produto(nome) no dicionário produtos;
b.Exibir todos os  produtos e  seus  respectivos  preços.  Defina  uma função   chamada   exibirProdutos(produtos) que recebe como parâmetro uma lista de produtos;
c.Remover um  produto específico. Defina  uma  função chamada removerProduto(produtos,  produto) que  recebe como parâmetro os produtos cadastrados e o produto a ser removido;
d.Exibir produto  mais  caro  dos  produtos  cadastros. Defina  uma função  chamada exibirCaroProduto(produtos) que recebe  como parâmetro uma lista de produtos; 
e.Exibir produto  mais  barato dos  produtos  cadastros. Defina  uma função  chamadaexibirCaroProduto(produtos) que  recebe  como parâmetro uma lista de produtos;
f.Crie uma função que exiba um menu com as opções:
i. Adicionar Produto;
ii.Listar Produtos;
iii.Remover Produto;
iv.Exibir o mais caro;
v.Exibir o mais barato.
'''

produtos = {}

def cadastrarProduto(produtos, produto, preco):
  produtos[produto] = preco
  print(produtos)
    
def exibirProdutos(produtos):
  for X in produtos.items():
   print(X)
  
def removerProduto(produto):
  del produtos[produto]
  print("Produto removido: ", produto)
  return produtos
  
def exibirCaroProduto(produtos):
  ProdutoCaro = max(produtos, key = produtos.get)
  PrecoCaro = produtos[ProdutoCaro]
  print("O produto mais caro é:", ProdutoCaro,)
  print("Preço: ", PrecoCaro)

def exibirBaratoProduto(produtos):
  ProdutoBarato = min(produtos, key = produtos.get)
  PrecoBarato = produtos[ProdutoBarato]
  print("O produto mais barato é: ", ProdutoBarato)
  print("Preço: ",PrecoBarato)
  
def main(Args=None):
    continuar = ("sim")
    while(continuar == "sim"):
      print("")
      print("(1) Cadastrar Produto")
      print("(2) Exibir Produtos")
      print("(3) Remover Produto")
      print("(4) Exibir produto mais caro")
      print("(5) Exibir Produto mais barato")
      print("(6) Sair")
      alternativa = int(input("Escolha uma das alternativas que foram propostas acima: "))
      print("")
      if (alternativa == 1):
        produto = str(input("Digite o nome do produto para cadastrar: "))
        preco = eval(input("Digite o preço do produto para cadastrar: "))
        cadastrarProduto(produtos, produto, preco)
      elif (alternativa == 2):
        exibirProdutos(produtos)
      elif (alternativa == 3):
        produto = str(input("Digite o nome do produto que você deseja remover: "))
        removerProduto(produtos, produto)
      elif (alternativa == 4):
        exibirCaroProduto(produtos)
      elif (alternativa == 5):
        exibirBaratoProduto(produtos)
      elif (alternativa == 6):
        continuar = ("não")
        print("Programa Finalizado")
      else:
        print("Alternativa de número inválido!")
if(__name__ == __name__):
  main()
