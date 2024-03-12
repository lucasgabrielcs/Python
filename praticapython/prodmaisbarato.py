# Faça um programa que pergunte o preço de 
# três produtos e informe qual produto você 
# deve comprar, sabendo que a decisão é 
# sempre pelo mais barato.

print("CADASTRE: ")
nome1=input("Digite o nome da mercadoria:")
preço1=float(input("Digite o preço: "))

nome2=input("Digite o nome da mercadoria 2:")
preço2=float(input("Digite o preço: "))

nome3=input("Digite o nome da mercadoria 3:")
preço3=float(input("Digite o preço: "))

nome1=preço1 and nome1
nome2=preço2 and nome2
nome3=preço3 and nome3

if preço1<preço2 and preço1<preço3:
 
 print("Você deve comprar o ", nome1)

elif preço2<preço1 and preço2<preço3:
 print("Você deve comprar o ",nome2)

else:
 print("Você deve comprar o ",nome3) 
