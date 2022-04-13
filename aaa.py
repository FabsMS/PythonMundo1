name = str(input("Digite aqui o seu nome: "))
relation = str(input("Você namora? "))

if relation == "sim":
    name2 = str(input("E qual é o nome do seu/sua namorado(a)? "))
    if name2 == "Fabricio" and name == "Luiza":
        print("Vocês realmente são um casal incrível, o melhor que já existiu!!")
    else:
        print(f"Até que são um casal legal, mas nunca chegarão aos pés de Fabricio e Luiza, sinto muito :/")
else:
    print("Então tá na hora de desencalhar ein")
