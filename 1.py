# Algoritmo da Amizade
ligar = input("Digite '1' se a pessoa atendeu, ou '0' se não atendeu\n")
while ligar == 0:
    ligar = input("Digite '1' se a pessoa atendeu, ou '0' se não atendeu\n")
    if ligar == 1:
        continue

fim = ("Comece uma amizade")

print("Convide para uma refeição")
convite = int(input("Digite '1' se a pessoa aceitou, ou '0' se não aceitou\n"))
if convite == 1:
    print(fim)
    exit() 
else:
    print("Ofereça uma bebida")

bebida = int(input("Digite '1' se a pessoa aceitou a bebida, ou '0' se não aceitou\n"))
if bebida == 1:
    print("Pergunte se prefere café, chá ou chocolate")
    print(fim)
    exit()
else:
    n = 3
    while n > 0:
        n = n - 1
        print("Pergunte sobre um interesse")
        interesse = int(input("Digite '1' se a pessoa teve interesse, ou '0' se não teve"))
        if interesse == 1:
            print ("Engage em uma conversa sobre o interesse em comum")
            print(fim)
            break
        elif:
                
        else:
            print("Tente novamente")

