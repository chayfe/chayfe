from random import randint
#from time import sleep
computador = randint(0, 5)
jogador = int(input('advinha: '))
if jogador == computador:
    print('Para bens')
else: 
    print('errou!!! era esse {} e não nesse {}!' .format(computador, jogador))