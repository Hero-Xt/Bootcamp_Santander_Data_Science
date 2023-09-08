'''
Uma função pode retornar mais de um valor
'''
def s():
    num1 = 0
    num2 = 2
    return num1, num2
print(s()) #retornando uma tupla
# da para acessar elemento por elemento da tupla
print(f"numero1: {s()[0]} numero2: {s()[1]}")

#argumentos nomeados
def carro(marca, modelo, ano):
    print(marca, modelo, ano)

carro(marca='ford', modelo='ka',ano=2019)

# ** PARA IDENTIFICAR QUE VAI PASSAR UM DICIONARIO COMO ARG
carro(**dict(marca='AUDI', modelo='R8', ano=2023))

# args * = tuplas
# kwargs ** = dicionario

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio',1999, 'ABC-1234', marca='Fiat', motor='1.00',combustivel='Flex')

def carro_2(*, marca, modelo, ano): # só para nomeação
    print(marca, modelo, ano)

carro_2(marca='ford', modelo='ka',ano=2019)

def criar_carro_2(modelo, ano, placa, /, * marca, motor, combustivel): #Hibrido
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio',1999, 'ABC-1234', marca='Fiat', motor='1.00',combustivel='Flex')


#posição = /
#nomeação = *
# e pode usar um hibrido

salario = 2000 #valiavel na raiz

def salario_bonus(bonus):
    global salario #chamando a variavel fora da função, utilizando a palavra reservada global
    salario += bonus
    return salario

print(salario_bonus(1000))