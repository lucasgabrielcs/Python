#Ler a temperatura de uma pessoa e exibir a 
#mensagem “Febre Alta” (temp ≥ 39), “Febril”
# (39 > temp ≥ 37) ou “Sem Febre” (temp < 37).

#implementar a temp da pessoa
#colocar if para (Febre alta)
#colocar elif para (Febril)
#colocar else para (Sem Febre)
#Imprimir resultado

print("DETECTOR DE FEBRE")
temp=float(input("Digite a sua temperatura: "))

if temp >=39:
    print("você está com Febre alta")
elif temp >=37:
    print("você está Febril")
else:
    print("Sem febre")