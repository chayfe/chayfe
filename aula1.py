nome = str(input('qual eh o seu nome:'))
print('seja bem vindo',nome, 'prazer em te conhecer')
print(nome.isupper)

n1 = str(input('primeiro numero:'))
n2 = str(input('segundo numero: '))
r = str((n1+n2))
print(r.isnumeric())

n1 = str(input('primeiro numero:'))
n2 = str(input('segundo numero: '))
r = str((n1+n2))
print(r.isupper())

n1 = str(input('primeiro numero:'))
n2 = str(input('segundo numero: '))
r = str((n1+n2))
print('resultado da soma é: ', r)
print('a soma entre', n1, 'e', n2, 'resultado: ', r)
print('a soma entre {} e {}'.format(n1,n2,r))