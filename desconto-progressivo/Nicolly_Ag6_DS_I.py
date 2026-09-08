valor_compra = float(input("Digite o valor total da compra: R$ "))

# Define o desconto de acordo com o valor da compra
if valor_compra < 200:
    desconto = 5
elif valor_compra < 300:
    desconto = 10
else:
    desconto = 15

valor_desconto = valor_compra * desconto / 100
valor_final = valor_compra - valor_desconto

print(f"\nDesconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")