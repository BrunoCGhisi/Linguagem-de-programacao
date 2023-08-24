#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:20,Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são:

t=int(input("Quantos voce trabalhou ? "))
i=int(input("Qual a sua idade?"))
if (i>=60):
    print("Pode se aposentar")
elif(t>=30):
    print("Pode se aposentar")
elif((i>=60) & (t>=25)):
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")