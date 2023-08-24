#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:17,Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):

h=float(input("Qual a sua altura?"))
r=int(input("Homem  = 1"
          "\nMulher = 2"))
if r==1:
    print(f"Seu peso ideal é : {(72.7 * h) - 58}")
elif r==2:
    print(f"Seu peso ideal é : {(62.1 * h) - 44.7}")
