#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:19, Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida.

n1=float(input("Numero 1"))
n2=float(input("Numero 2"))
r=int(input("Somar       = 1"
          "\nSubtrair    = 2"
          "\nMultiplicar = 3"
            "\nDividir   = 4"))
while True:
    if r==1:
        print(f"{n1+n2}")
    elif r==2:
        if n1>n2:
            print(f"{n1 - n2}")
        else:
            print(f"{n2 - n1}")
    elif r==3:
        print(f"{n1 * n2}")
    elif r==4:
        print(f"{n1 / n2}")
    else:
        break
