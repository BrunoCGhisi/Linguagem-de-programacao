#1º .append() -> adiciona um item no fim da lista
a = ["Matheus"]

print(a)

print(".append() -> adiciona um item no fim da lista : ")

a.append("Maria Joana")
print(a)
# Ai aqui se tornou: a = ["Matheus", "Maria Joana"]

#2º .insert() -> adiciona o item em uma posição declarada da lista

print("insert() -> adiciona o item em uma posição declarada da lista : ")
a.insert(0, "Bruno")
print(a)
print("E eu posso colocar numeros tambem : ")
a.insert(0, 3.45)
print(a)

#E para alterar um item de uma lista
print("#E para alterar um item de uma lista : ")
a[0] = ("André")
print(a)

#Pegando itens a partir de um intervalo de index

print(a[:3],"Todos os valores antes do 3")
print(a[3:],"Todos os valores depois do 3")
print(a[1:3],"Todos os valores entre 1 e 3 ")


#3º del -> delete pelo index do item na lista
#Removendo itens da minha lista

#print("Removendo itens da minha lista : ")

#print(a,"(Versão normal)")
#del a[0:2] #delete pelo index do item na lista
#print(a,"(Depois do delete, entre 0 e 1)")

#3.5º deletando um item da lista pelo nome do item
#print("Deletando por a.remove('Matheus')")
#print(a, "Versao normal")
#a.remove("Matheus")
#print(a, "depois do delete")

#3.75º deletando um item da lista pelo index do item porém salvando um novo

#4º Limpando uma nova lista

#a.clear()
#print(a)

#5ºCopiando uma lista

#c= a.copy()
#print(a)
#print(c)

#6º Juntando listas
#d = a + c
#print(d)

#7º contando itens
#print(a.count("Matheus"))    #Quantas vezes aparece Andre na lista

#print(len(a))              #Numeros totais na lista

#8º Procurando itens
#print(a.index("Matheus")


