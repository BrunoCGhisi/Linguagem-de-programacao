#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:16,Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão.

o=0
r=int(input("Voce quer passar farenheit para Celsius? = 1"
          "\nou quer passar Celsius para farenheit? = 2"))
if r==1:
    tempF = float(input("Quantos Fº ? "))
    print(f"C{(tempF-32)/9}ª")
elif r==2:
    tempC = float(input("Quantos Cº ? "))
    print(f"C{(tempC*1.8)+32}ª")
