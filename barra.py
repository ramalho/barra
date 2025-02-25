import time
from collections.abc import Iterable

ESQUERDA, MIOLO, DIREITA = '[=]'
LARG_MIOLO = 76


def barra(qt_itens:int, iteravel:Iterable):
    grafico = ESQUERDA + ' ' * LARG_MIOLO + DIREITA
    print(grafico, end='', flush=True)
    for n, item in enumerate(iteravel, 1):
        preenchido = int(LARG_MIOLO * n / qt_itens)
        conteudo = MIOLO * preenchido + ' ' * (LARG_MIOLO - preenchido)
        grafico = ESQUERDA + conteudo + DIREITA
        print('\r' + grafico, end='', flush=True)
        yield item
    miolo = ' ' * (LARG_MIOLO + len(ESQUERDA) + len(DIREITA))
    print('\r' + miolo + '\r', end='', flush=True)
