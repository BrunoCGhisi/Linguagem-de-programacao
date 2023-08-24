#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:22, ) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
#Desconsiderando o valor 1000 da parada.

w= -1
lista = []
while w != 1000:
    lista.append(input("digite  algo: "))
    w= int(input("Quer continuar? Se sim digite 1 ; Se não digite 1000 "))
print(lista)
print(len(lista))