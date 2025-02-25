import time

from barra import barra

def animar(passos, tempo):
    for _ in barra(passos, range(passos)):
        time.sleep(tempo/passos)


print('Pensando por 3s...')
animar(100, 3)
print('Resposta = 42')