#Aluno:Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:13, Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles

lista = []
for i in range(5):
    lista.append(int(input("digite  algo: ")))
soma = sum(lista)
print(lista)
print(soma)
