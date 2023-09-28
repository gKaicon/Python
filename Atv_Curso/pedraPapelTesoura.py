from os import system
import random

comput = random.choice([0,2,5])

dados = {"nome": "0", "opcao": -1 }

dados['nome'] = input('Digite seu nome: ')
dados['opcao'] = int(input('Digite sua opção: '))

if dados['opcao'] == 0:
    opV = "Pedra"
if dados['opcao'] == 2:
    opV = "Tesoura"
if dados['opcao'] == 5:
    opV = "Papel"
if comput == 0:
    opC = "Pedra"
if comput == 2:
    opC = "Tesoura"
if comput == 5:
    opC = "Papel"
    
system("cls")

print(dados['nome'], "pôs: ", opV, "\tComputador: pôs", opC)

if dados['opcao'] == comput:
    print("Empatou")
if dados['opcao'] == 0 and comput == 2:
    print(dados['nome'] + " ganhou")
if dados['opcao'] == 0 and comput == 5:
    print("Computador venceu.")
if dados['opcao'] == 2 and comput == 5:
    print(dados['nome'] + " ganhou")
if dados['opcao'] == 2 and comput == 0:
    print("Computador venceu.")
if dados['opcao'] == 5 and comput == 0:
    print(dados['nome'] + " ganhou")
if dados['opcao'] == 5 and comput == 2:
    print("Computador venceu.")