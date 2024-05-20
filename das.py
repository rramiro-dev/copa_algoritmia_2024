'''tipo = ['Oro', 'Espada', 'Basto', 'Copa']

print(
    list([str(carta) + f' de {tipo[palo]}' for carta in range(1, 12 + 1)] for palo in range(len(tipo)))
)'''

vocales =  ['A', 'E', 'I', 'O', 'U']

texto = input('pasame la data')

for letra in texto:
    if letra in vocales:
        letra.upper()


print()