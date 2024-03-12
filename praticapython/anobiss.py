#Faça um Programa que peça para entrar com 
# um ano (inteiro com 4 dígitos) e determine se 
# o mesmo é ou não bissexto (divisível por 4).

ano=(input("digite um ano bissexto inteiro com 4 digitos: "))

if len(ano)==4:
     
    ano = int(ano)

    if ano % 4 == 0:
        print("O ano ",ano," é bissexto")
    else:
        print("O ano ",ano," não é bissexto")
    
    
else:
    print("Digite um numero com 4 digitos!")    