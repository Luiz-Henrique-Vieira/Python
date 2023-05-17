#criação da lista
nomes = [] #ou nomes = list()
#armazenar valores na lista
for i in range(5):
    n = input('Digite um nome: ')
    nomes.append(n) #adiciona no final da lista #nomes.insert(i,n)[
    
print(nomes) #mostra os itens da lista
print(len(nomes)) #quantidade de itens da lista
#exlui um item da lista
nome = input('Digite um nome pra remover da lista; ')
if nome in nomes:
    nomes.remove(nome) #remove o nome da lista
    print(nomes) #mostra os itens da lista
    print(len(nomes)) #mostra o tamanho da lista
else:
    print('Nome não encontrado')