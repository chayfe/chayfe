#ano = int(input('Que ano quer saber?'))

#if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
#    print('O ano {} e bissexto' .format(ano))
#else: 
#    print("O ano {} não e bissexto" .format(ano))

from datetime import date
ano = int(input("qual ano: "))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
   if ano >= 1582:
      print("o ano {} é bi e gregoriano".format(ano))
   else: 
      print("o ano {} é bi mas nao é gregoriano".format(ano)) 
else:
    if ano >= 1582:
      print("o ano {} nao e bi e nao é gregoriano".format(ano))
    else: 
      print("o ano {} nao é bi e nao é gregoriano".format(ano))      