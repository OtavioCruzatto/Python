"""
Jogo da forca - V5.0

Autor: Otavio Cruzatto
Data de criacao: 23/07/218
Data de modificacao: 24/07/2018

Caracteristicas desta versao:
  - As palavras sao selecionadas aleatoriamente
  - Durante a mesma secaoo de execucaoo, nenhuma palavra eh repetida
  - Pode-se digitar letras maiusculas e minusculas
  - O arquivo aonde se encontram as palavras eh aberto e fechado
  - O caracter utilizado para cada letra eh o underscore (_)
  - Na setima letra errada, a palavra eh revelada
  - A palavra que eh pega do arquivo eh passada inteira para maiuscula
"""

import random

print("### Jogo da forca ###")

ref_arquivo = open("palavras_dicas.txt","r")
palavras_chave = ref_arquivo.readlines()
ref_arquivo.close()
letras_utilizadas = []
letras_descobertas = []
palavras_utilizadas = []
acertou_palavra = False
deseja_jogar = True
quantidade_de_erros = 0

while(deseja_jogar == True):

    palavra = palavras_chave[random.randrange(0, len(palavras_chave))]
    while palavra in palavras_utilizadas:
        palavra = palavras_chave[random.randrange(0, len(palavras_chave))]

    palavras_utilizadas.append(palavra)
    palavra = palavra.split(",")
    palavra_selecionada = palavra[0].upper()
    dica = palavra[1].strip()

    for contador in range(0, len(palavra_selecionada)):
        letras_descobertas.append("_")

    print("\n\nDica 1: A palavra possui " + str(len(palavra_selecionada)) + " letras!")
    print("Dica 2: " + dica.capitalize())

    while(acertou_palavra == False and quantidade_de_erros < 7):
        letra_chutada = (str(input("\n\nDigite uma letra: "))).upper()

        if letra_chutada in letras_utilizadas:
            print("Voce ja digitou esta letra...")
            letras_utilizadas.append(letra_chutada)
        else:
            letras_utilizadas.append(letra_chutada)
            if letra_chutada in palavra_selecionada:
                for contador in range(0, len(palavra_selecionada)):
                    if letra_chutada == palavra_selecionada[contador]:
                        letras_descobertas[contador] = letra_chutada
            else:
                quantidade_de_erros = quantidade_de_erros + 1
                print("Voce errou: " + str(quantidade_de_erros) + " vezes")

        for contador in range(0, len(palavra_selecionada)):
            print(letras_descobertas[contador], end=' ')

        if "_" in letras_descobertas:
            acertou_palavra = False
        else:
            acertou_palavra = True

    if quantidade_de_erros == 7:
        print("\n\nLamento, voce errou :(")
        print("A palavra era: " + palavra_selecionada)
        print()
        jogar_novamente = (str(input("Deseja jogar novamente? [y/n]"))).upper()
    else:
        print("\n\nParabens, voce conseguiu!!!")
        jogar_novamente = (str(input("Deseja jogar novamente? [y/n]"))).upper()

    if jogar_novamente == "Y":
        deseja_jogar = True
        acertou_palavra = False
        letras_descobertas = []
        letras_utilizadas = []
        quantidade_de_erros = 0
    else:
        deseja_jogar = False
        print("Obrigado por jogar :)")

    if len(palavras_utilizadas) == len(palavras_chave):
        print("Palavras esgotadas, em breve teremos mais...")
        print("Obrigado por jogar :)")
        deseja_jogar = False

