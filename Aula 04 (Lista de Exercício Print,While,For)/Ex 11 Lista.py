#Aluno:Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:11, Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.

Name=input("Diga seu nome")
H = float(input("Quantas horas voce trabalha por mes?"))
R = float(input("Quanto vale sua hora?"))

Sal = (H*R)
INSS= (Sal*2)/100
print(INSS)
print(f"{Name} você recebe {Sal-INSS}")