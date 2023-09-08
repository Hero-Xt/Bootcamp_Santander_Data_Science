palavra = input('Digite uma palavra').lower()
vogais = 'aeiou'
lido = ""
for letras in palavra:
    if letras in vogais:
        lido += letras

print(f'fora lozalizadas as vogais: {lido}')

for cont in range(11):
    print(f'{cont}')
    