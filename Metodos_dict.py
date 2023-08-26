pessoa = {'nome': 'Gabriel', 'idade': 22}
pessoa = dict(nome='Gabriel', idade=22)
pessoa['telefone'] = '2344-4638'

#pessoa.clear() #limpa o dicionario
pessoa.copy() #copia o dicionario
#cria chaves em branco, ou com um valor
pessoa.fromkeys(['nome','telefone'])
pessoa.fromkeys(['nome','telefone'], 'vazio')

#pegar elemento do dicionario, se não tiver nada ele retorna NONE
print(pessoa.get('nome'))
pessoa.item() #retorna uma lista de tuplas
pessoa.keys() #retorna as chaves
pessoa.pop('nome', {}) # se não achar ele retorna um valor padrão
pessoa.popitem() #apaga o primeiro item
pessoa.setdefault('pente') # se não tiver no dicionario ele adiciona ele
pessoa.update() #atualiza o dicionario com outro dicionario
pessoa.values() #retorna só os valores

'nome' in pessoa
