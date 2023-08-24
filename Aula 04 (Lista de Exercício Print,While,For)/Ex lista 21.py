#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:20,Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são:

n1=float(input("Numero 1"))
n2=float(input("Numero 2"))
r=int(input("Somar       = 1"
          "\nMultiplicar    = 2"
          "\nMaior = 3"
            "\nMenor   = 4"
            "\nSair do Programa = Qualquer outro digito"))
while True:
    if r==1:
        print(f"{n1+n2}")
    elif r==2:
        print(f"{n1*n2}")
    elif r==3:
        if (n1>n2):
            print(f"{n1}")
        elif (n2>n1):
            print(f"{n2}")
    else:
        break

