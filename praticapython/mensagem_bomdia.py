# Faça um Programa que pergunte em que turno a 
# pessoa estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor 
# Inválido!", conforme o caso.

turno=input("Digite em que turno você estuda M(Manhã),V(Tarde) e N(Noite) ? ")

turno = turno.upper()

if turno=="M":
    print("Bom dia!")
elif turno=="V":
    print("Boa tarde!")
elif turno=="N":
    print("Boa noite!")
else:
    print("Valor Inválido!")