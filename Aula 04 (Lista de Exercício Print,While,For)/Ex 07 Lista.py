#Aluno:Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:07,Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
#de aumento.

valor  = float(input("Diga quantos custa este produto, e eu te direi com 5% desconto - 15% aumento"))
valorD = (valor*5)/100
print(valor-valorD)
valorA = (valor*15)/100
print(valor+valorA)