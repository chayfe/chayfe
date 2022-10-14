while True:
    from random import randint
    n=randint(1,5)
    print (n)
    jogo = 0
    adivinha=int(input('adivinha '))
    if adivinha==0:
        break
    for jogo in range (1,3+1):
        
        
        if adivinha==n:
            print('para bens ')
            break
        else:
            print('vai de volta ')    
            