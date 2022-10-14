
#salário = float(input("Digite o salário: "))
#base = salário
#imposto = 0
#if base > 85.528:
#     imposto = imposto + ((base - 85.528) * 0.18)
#     base = 3000
#if base > 85.528:
#     imposto = imposto + ((base - 1000) * 0.32) 

#print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salário, imposto))


salario = float(input("quanto vc ganha? "))
taxa = 0
if salario <= 85528:
     taxa = ((salario*18)/100) - 556.02
else:
     taxa = (((salario - 85528)*32)/100)+14839.02

taxa = round(taxa,2)
print("a taxa e ", taxa, "reais")          