#Obj:Ler o valor de um cheque e escrever o quanto vai ser recolhido de CPMF. 
#Considere que imposto recolhe uma taxa de 0,3%. Imprimir o valor do imposto.

#Fazer:
#Implantar o valor do cheque
#recolher uma taxa de 0,3%
#mostrar quanto vai ser recolhido
#imprimir o valor final

cheque=float(input("Digite o valor do cheque: "))
imposto=(cheque*0.003)
print("vai ser recolhido de CPMF um imposto de(0,3%): ",imposto)

valorfinal=cheque-imposto
print("o valor final vai ser de: ",valorfinal)