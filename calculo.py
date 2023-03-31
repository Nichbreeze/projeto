motoboys = []

# Solicita a entrada dos dados para cada motoboy e armazena em uma lista de dicionários
for i in range(1):
    corridas = int(input(f"Quantas corridas o motoboy {i+1} fez? "))
    km_corridas = []
    for j in range(corridas):
        km_corrida = float(input(f"Digite a distância da corrida {j+1} (em km): "))
        km_corridas.append(km_corrida)
    motoboy = {"corridas": corridas, "km_corridas": km_corridas}
    motoboys.append(motoboy)

# Calcula o valor para cada motoboy e acumula o lucro total e os gastos totais
lucro_total = 0
gastos_total = 0
for i, motoboy in enumerate(motoboys):
    valor_motorista = 0
    valor_empresa = 0
    for km_corrida in motoboy["km_corridas"]:
        if km_corrida <= 4:
            valor_corrida = 9
        else:
            valor_corrida = 9 + 1.3*(km_corrida-4)
        valor_motorista += valor_corrida
        if km_corrida <= 4:
            valor_corrida_empresa = 10
        else:
            valor_corrida_empresa = 10 + 1.5*(km_corrida-4)
        valor_empresa += valor_corrida_empresa
    valor_api = motoboy["corridas"] * 0.15
    valor_total = valor_empresa - valor_motorista - valor_api
    gastos_total += valor_motorista + valor_api
    lucro_total += valor_empresa - valor_motorista - valor_api
    print(f"Motoboy {i+1}:")
    print(f"Quantidade de corridas feitas : {motoboy['corridas']}")
    print(f"Total de km corridos pelo motoboy: {sum(motoboy['km_corridas']):.2f} km")
    print(f"repasse total para a empresa: R${valor_empresa:.2f}")
    print(f"Valor a pagar para o motoboy: R${valor_motorista:.2f}")
    print(f"Valor a pagar para a API: R${valor_api:.2f}")



print(f"Gastos totais da empresa: R${gastos_total:.2f}")
print(f"Lucro total da empresa: R${lucro_total:.2f}")

