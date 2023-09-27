# Criando lista de animais
animals = ["cachorro", "gato", "coelho", "papagaio", "gato", "coelho"]

#contando quantos gatos há na lista
animals.count("gato")

#contando quantos leões há na lista
animals.count("leão")

#encontrando o primeiro indice do primeiro coelho da lista
animals.index("coelho")

#encontrando o primeiro indice do primeiro coelho da lista, a partir do indice 3
animals.index("coelho", 3)

#adicionando o elefante
animals.append("elefante")

#remove o ultimo da lista
animals.pop()

#invertendo em ordem alfabetica
animals.sort()