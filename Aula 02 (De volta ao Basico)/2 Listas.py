#cricao de lista

nomes = ["Bruno", "Marcelo", "Maria", "Mariane", "Marcos"]
print(nomes[4])
nomes[2] = "1"
print(nomes)

#criacao de tuplas
carros = ("gol", "uno", "celta", "fusca", "brasilia")
print(carros[0])
#carros[0] = "mercedes"         ###vai da erro

#criacao de dicionario

peso = {"amanda": 55.6, "joao": 70.6, "artur": 55.6}
print(peso)
#####################

v1= int(input("Digite um valor"))
v2= int(input("Digite um valor"))

n1=  int(input("digite um valor:  "))

print(n1.isnumeric())
print(n1.isalpha())
print(n1.isdecimal())
print(n1.isalnum())
print(n1.islower())
print(n1.isupper())
print(n1.istitle())

s= int(v1) + int(v2)
print(f"a soma dos valores {v1} e {v2} resulta na soma {v1+v2}")

