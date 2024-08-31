INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)
 def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada do usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
 import json

# Carregar o arquivo JSON
with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamentos = data['faturamento']
faturamentos = [f for f in faturamentos if f > 0]

# Cálculo
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_media = sum(1 for f in faturamentos if f > media_mensal)

# Resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
 # Dados dos faturamentos
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

# Cálculo dos percentuais
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

# Resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
def inverter_string(s):
    resultado = ''
    for char in s:
        resultado = char + resultado
    return resultado

# Entrada do usuário
entrada = input("Digite a string para inverter: ")
print("String invertida:", inverter_string(entrada))