"""If ternário permite escrever uma condição em uma unica linha.
Ele é composto por três partes, a primeira parte é o  retorno
caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica 
e a terceira parte é o retorno caso a expressão não seja atendida"""

saldo = 2000
saque = 2000
status = 'Sucesso' if saldo >= saque else 'Falha'

print(f"{status} so realizar o saque!")

saque = 20000

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f"{status} so realizar o saque!")
