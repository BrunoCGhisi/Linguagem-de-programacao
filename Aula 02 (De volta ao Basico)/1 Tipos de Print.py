"""nome = "Bruno"
idade= 17

print ("Ola", nome, "voce tem", idade, "anos")
print ("Ola " + nome + "voce tem 17 anos")
print (f"Ola  {nome} voce tem {idade} anos") #Vai ter que usar esse agora Bruno /: meeeeee

n1= input("Qual seria o seu nome ? ")
n2= input("Qual seria o seu nome ? ")
n3= input("Qual seria o seu nome ? ")

print (n1,n2,n3)
#ou dessa vez o modo certo
print (f"{n1} \n{n2} \n{n3}") #\n É a tal de quebra de linha

###
###
###

dia = 20
mes = 2
ano = 2023
print ("João estava andanddo na padaria" , end= ", " ) ##Coloca algo no final de seu print
print ("porque estava com fome")
print (dia,mes,ano, sep="/")      """                     ##coloca algo para separar as suas variaveis

#########

a = input("Digite seu nome : ")
b = ("Joaquim")
print(f"Seja bem vindo {a:20}")
print(f"Seja bem vindo {a:>20} e {b}")  #esquerda
print(f"Seja bem vindo {a:<20} e {b}")  #direita
print(f"Seja bem vindo {a:^20} e {b}")  #
print(f"Seja bem vindo {a:-^20}")