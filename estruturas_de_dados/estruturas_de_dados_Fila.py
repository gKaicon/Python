#stack
from collections import deque

frutas = deque(["maçã", "banana", "laranja"])

frutas.append("uva")
frutas.append("abacaxi")

frutas.popleft()

frutas.popleft()