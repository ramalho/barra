import time

from barra import barra

def fatorial(n, fps=0):
    """Uma implementação dramática do fatorial!"""
    fps = fps if fps > 0 else n
    produto = 1
    for item in barra(n, range(1, n+1)):
        time.sleep(1/fps)
        produto *= item
    return produto

for n in range(6, 55, 8):
    print(f'{n:2d}! = {fatorial(n)}')