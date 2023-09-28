from os import system
from random import choice

MAX_TENTATIVAS = 6

animais = [
    "elefante", "girafa", "tigre", "zebra", "rinoceronte", "canguru", "panda", "gorila", "koala", 
    "tucano", "orca", "pinguim", "alce", "camelo", "suricata", "lobo", "coala", "leopardo", "cavalo", 
    "gato", "cachorro", "urso", "vaca"]

frutas = [
   "maça", "banana", "laranja", "uva", "morango", "pera", "abacaxi", "manga", "kiwi", "melancia", "limao", 
   "pessego", "cereja", "coco", "ameixa", "framboesa", "melao", "abacate", "goiaba", "maracuja", "tangerina", 
   "pitaya", "caqui"]

class Forca():
    
    def __init__(self):
        self.__resetar()
        
    def __resetar(self):
        self.__tentativa = 0
        self.__palavra = []
        self.__letrasUtilizadas = set()
        self.__dicionario = {}
        
    def jogar(self) -> None:
        self.__resetar()
        palavra_sorteada = self.__sortearPalavra()
        
        if palavra_sorteada is None:
            return
        self.__palavra = ['_' for caracter in palavra_sorteada]
        self.__criarDicionario(palavra_sorteada)
        while True:
            system("cls")
            print(', '.join(self.__letrasUtilizadas))
            print("Número de erros: ", self.__tentativa, "\tNúmero de letras da palavra: ", len(palavra_sorteada))
            print("{:^24}".format(''.join(self.__palavra)))
            chute:str = input("Digite uma letra: ")
            self.__fazerChute(chute)
            if self.__tentativa == MAX_TENTATIVAS and len(self.__dicionario) > 0:
                print("Perdeu")
                print("A palavra sorteada era ", palavra_sorteada)
            elif not len(self.__dicionario):
                print("A palavra sorteada é ", palavra_sorteada)
                print("Ganhou")
        
    def __sortearPalavra(self) -> None | str:
        while True:
            print("1 - Animais\n2 - Frutas\n3 - Sair")
            opcao = int(input("Digite sua opção: "))
            system("cls")
            if opcao == 1:
                return choice(animais)
            if opcao == 2:
                return choice(animais)
            if opcao == 3:
                return
            
    def __criarDicionario(self, palavra:str) -> None:
        self.__dicionario = {}
        for i in range(len(palavra)):
            self.__dicionario.setdefault(palavra[i],[]).append(i)
            
    def __fazerChute(self, chute:str) -> None:
        if not str.isalpha(chute):
            return
        if chute in self.__dicionario:
            for i in self.__dicionario[chute]:
                self.__palavra[i] = chute
            self.__dicionario.pop(chute)
        elif chute not in self.__letrasUtilizadas:
            self.__tentativa += 1
        self.__letrasUtilizadas.add(chute)

forca = Forca().jogar()