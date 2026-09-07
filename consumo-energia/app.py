print(" CALCULADORA DE CONSUMO DE ENERGIA ")
print("-" * 45)

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

# Classificação do consumo
if consumo_mensal < 30:
    classificacao = "🟢 Baixo consumo"
elif consumo_mensal <= 100:
    classificacao = "🟡 Consumo moderado"
else:
    classificacao = "🔴 Alto consumo"

# Resultado
print("\n RESULTADO")
print("-" * 45)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} por mês")
print(f"Classificação: {classificacao}")