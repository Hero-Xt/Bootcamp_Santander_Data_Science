lista = [1,3,5,-1,0]
lista.append(1) #adiciona item na lista
l2 = lista.copy() #copiar a lista
lista.count('vermelho') #conta os elementos
lista.count(2)
lista.extend([2, 3, 4]) #adiciona item, ou itens a lista
lista.index('uva') #indica a posição da primeira aparição
lista.pop() #tirar o utimo elemento da lista
lista.pop(3) #remove o item que quiser pelo indice
lista.remove('C') #remove a primeira ocorrencia doitem pelo que ele é 
lista.reverse() #coloca a lista ao contrario
lista.sort() #ordena a lista
lista.sort(reverse=True) #oderna de forma contraria
lista.sort(key=lambda x: len(x)) #ordena pelo tamanho do maior para o menor
lista.sort(key=lambda x: len(x), reverse=True) #oderna pelo tamanho inversa
lista.len() #lamanho da lista
sorted(lista)
sorted(lista, key=lambda x: len(x))
sorted(lista, key=lambda x: len(x), reverse=True)
