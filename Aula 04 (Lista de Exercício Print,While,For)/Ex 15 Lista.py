#Aluno: Bruno Costa Ghisi 2190
#Professora: Mariane
#Linguagem de Programação
#Exercício:15, Verifique temperatura e resposta adequada

temp = float(input("Qual a temperatura"))
if (temp>25):
    print("Quente")
elif (temp<24 or temp>15):
    print("Agradável")
else:
    print("frio")