#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:24, Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.




while True:
    n=float(input("Diga uma nota entre 0 a 10"))
    if (n>10.1)or(n<0):
        break
