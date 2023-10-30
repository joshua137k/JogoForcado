import random
import os
from game import game



def main_menu(words1,words2):
  words = words1

  print(
      "ESCOLHA \n 1)palavras sem acentos nem cedilhas \n 2)palavras com acentos ou cedilhas. \n 3)palavras de ambos os tipos"
  )
  while True:
    i = input(">:")
    match(i):
      case "1":
        words = words1 # palavras sem acentos nem cedilhas.
        break
      case "2":
        words = words2 # palavras com acentos ou cedilhas.
        break
      case  "3":
        words = words1 + words2 # palavras de ambos os tipos
        break
      case _:
        print("Isso não é uma opção")

  return words


def RepeatGame():
  print("Você quer continuar a jogar?\n1)Sim\n2)Não")
  while True:
    i = input(">:")
    match(i):
      case "1":
        return False
        break
      case "2":
        return True
        break
      case _:
        print("Isso não é uma opção")

  return words


#funcao para escolher a biblioteca de palavras com base na resposta do usuario
def main():
  from wordlist import words1, words2

  while True:
    os.system('clear')

    words = main_menu(words1,words2)

    # Escolhe palavra aleatoriamente
    secret = random.choice(words).upper()
    #print(secret)
    os.system('clear')
    game(secret)
    if RepeatGame():
      break



if __name__ == "__main__":
  os.system('clear')
  main()

