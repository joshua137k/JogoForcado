# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [117462, 117468, 115799]

import os
from ferramentas import LetrasAcento, printSecretWord, printForca, tratamento, VerifyLetraInWord





#funcao para verificar se o jogador acertou e marcar seus lst_er e acertos
def game(word):
  lst_desc = [] # lista de letras corretas
  lst_er = [] # lista de letras erradas

  printForca(word, lst_desc, len(lst_er))
  print(printSecretWord(word, lst_desc, lst_er))
  print("")
  while True:

    ltr = input(">:")  # digitar Letra

    ltr = tratamento(ltr)

    if ltr == "FALSE!":  # se tratamento retornar a string "FALSE!" ele reinicia o loop
      continue

    if ltr in lst_er or ltr in lst_desc:
      print("Você ja digitou essa letra antes")
      continue

    ltr = LetrasAcento(ltr, word)

    acertou = VerifyLetraInWord(ltr, word, lst_desc, lst_er)

    if len(lst_er) > 5:
      print("Você perdeu a palavra era ", word)
      break
      
    os.system('clear')

    
    printForca(word, lst_desc, len(lst_er))
    newW = printSecretWord(word, lst_desc, lst_er)
    print(newW)

    if acertou:
      print("voce acertou uma letra :D")
    else:
      print("voce errou :(")

    print("")
    if newW == word:
      print("voce ganhou :D")
      break

