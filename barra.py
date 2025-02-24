import time
from collections.abc import Iterable

LARGURA = 78
ESQUERDA = '['
DIREITA = ']'
MIOLO = '='

def barra(unidades:int, iteravel:Iterable):
    grafico = ESQUERDA + ' ' * LARGURA + DIREITA
    print(grafico, end='', flush=True)
    for n, item in enumerate(iteravel, 1):
        preenchido = int(n/unidades * LARGURA)
        conteudo = MIOLO * preenchido + ' ' * (LARGURA - preenchido)
        grafico = ESQUERDA + conteudo + DIREITA
        print('\r' + grafico, end='', flush=True)
        yield item
    print()


resultados = []
for item in barra(10, range(100)):
    time.sleep(.01)
    resultados.append(item*10)

print(resultados)