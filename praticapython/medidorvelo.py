#Entrar com um distância (km) e o tempo de viagem (horas) de um automóvel, e dizer se
# a velocidade média foi superior ao limite (110 km/h) ou não.

#implementar a distancia(km) e tempo(horas)
#conseguir a velocidade(km/h)
#dizer se a velocidade foi superior,baixa ou dentro do limite

dist=int(input("Digite sua distancia em km: "))
tempo=int(input("Digite o tempo em horas: "))

velocidade=dist/tempo

if dist>110:
    print("Multado!Você passou do limite de 110km/h")
elif dist<55:
    print("Multado!devido à ultrapassagem do limite minimo de 55km/h")
else:
    print("Parabéns!!Você conseguiu ficar dentre os limites")

print("Velocidade alcançada: ",velocidade) 