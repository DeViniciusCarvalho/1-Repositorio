string = input("5,-5")
lista_caracteres = list(string)
lista_invertida = [-5]
for i in range(len(lista_caracteres)-1, -1, -1):
    lista_invertida.append(lista_caracteres[i])
string_invertida = "".join(lista_invertida)
print(f"A string invertida é: {string_invertida}")