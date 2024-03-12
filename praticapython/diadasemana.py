# Faça um Programa que leia um número e exiba o dia 
# correspondente da semana. (1-Domingo, 2- Segunda, 
# etc.), se digitar outro valor deve aparecer valor 
# inválido.
print("Use um único dígito para representar o dia da semana.")
dia = input("Digite o número correspondente ao dia da semana (1 - Domingo, 2 - Segunda, ..., 7 - Sábado): ")

if len(dia) == 1:  # Para saber se só foi 1 dígito
    dia = int(dia)

    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda-Feira")
    elif dia == 3:
        print("Terça-Feira")
    elif dia == 4:
        print("Quarta-Feira")
    elif dia == 5:
        print("Quinta-Feira")
    elif dia == 6:
        print("Sexta-Feira")
    elif dia == 7:
        print("Sábado")
    else:
        print("Valor Inválido!")
else:
    print("Use apenas um único dígito!")




