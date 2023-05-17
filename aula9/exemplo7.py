text = input('Digite um texto: ')
pontuacao = [".", ",",":",";","!", "?"]

#remove os sinais de pontuação

for p in pontuacao:
    text = text.replace(p, " ")


#split devolve lista com palavras como itens
numero_palavras = len(text.split())
print(f'O numero de palavras é: {numero_palavras}')