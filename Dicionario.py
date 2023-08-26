pessoa = {'nome': 'Gabriel', 'idade': 22}
pessoa = dict(nome='Gabriel', idade=22)
pessoa['telefone'] = '2344-4638'
print(pessoa)

#pessoa[nome]
print(pessoa['nome'])

pessoa['nome'] = "Hero-Xt"

print(pessoa)

contatos = {
    'gabriel7mz3256@gmail.com' : dict(nome='Gabriel', idade=22),
    'ghnjdoo@gmail.com' : {'nome' : 'Pedro', 'idade': 40},
    'maria22909@gmail.com' : dict(nome='Maria', idade=49),
}
print('Part 2')
print(contatos['gabriel7mz3256@gmail.com']['nome'])
print(contatos['gabriel7mz3256@gmail.com']['idade'])
print(contatos['maria22909@gmail.com'])

for chave, valor in contatos.items():
    print(chave, valor)


