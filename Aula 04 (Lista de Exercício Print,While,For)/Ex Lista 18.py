#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:18, Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

n1=float(input("Qual a sua primeira nota (Peso 5.0)"))
n2=float(input("Qual a sua segunda nota (Peso 5.0)"))
n3=float(input("Qual a sua terceira nota (Peso 10.0)"))

while  True:

    if n1>5.1:
        print("Nota invalida")
        break
    elif n2>5.1:
        print("Nota invalida")
        break
    elif n3>10.1:
        print("Nota invalida")
        break

media1 =  (n1+n2)/2
print(f"{(media1+n3)/2}")