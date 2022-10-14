import math
n = int(input("diga um numero: "))
raiz = math.sqrt(n)
print("a raiz de {} = {}".format(n,raiz))
print("a raiz de {} = {}".format(n,math.ceil(raiz)))
print("a raiz de {} = {}".format(n,math.floor(raiz)))
print("a raiz de {} = {:.2f}".format(n,raiz))