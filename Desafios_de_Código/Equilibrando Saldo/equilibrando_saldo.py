# Entrada do Saudo
saldo_atual = float(input())
# Valor das transações
valor_deposito = float(input())
valor_retirada = float(input())
# Atualizando Saldo
saldo_atual += valor_deposito - valor_retirada
# Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f"Saldo atualizado na conta: {saldo_atual:.1f}")
