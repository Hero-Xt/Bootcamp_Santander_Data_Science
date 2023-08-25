"""set = elemina os lementos duplicados em uma lista"""
print(set([1, 2, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
#não confia na ordem
print(set('abacaixi')) # {a b c i x}

#DECLARAÇÃÕ DE CONJUNTO
linguagens = {'python', 'Java', 'python'}
print(linguagens)

#conjuntos não suportam indexsação
#para obter um elemento converte em uma lista
#set(linguagens) ERRO
linguagens = list(linguagens)
print(linguagens)
print(linguagens[0])

conja = {1, 2, 3}
conjb = {2, 3, 4}

print(conja.union(conjb))
print(conja.intersection(conjb))
print(conja.difference(conjb))
print(conjb.difference(conja))
print(conjb.symmetric_difference(conja))
print(conja.issubset(conjb)) # os elementos de a estão em b
print(conjb.issubset(conja)) # os elementod de b estão em a
print(conja.issubset(conjb)) # todos  os elementos de a estão em b
print(conjb.issubset(conja)) # tdoos os elementod de b estão em a
print(conja.isdisjoint(conjb)) #conjuntos não se tocam
print(conjb.isdisjoint(conja)) #conjuntos não se tocam
print(conjb.add(25))
print(conjb.clear()) #apaga
print(conjb.copy())
print(conjb.discard(1))
print(conjb.discard(-1)) # não da erro se não tiver valor
print(conjb.pop()) #apaga o primeiro valor
print(conjb.remove(25)) #remove o elemento, se não tiver da erro
print(1 in conja)
