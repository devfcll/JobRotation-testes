import json

# abre o arquivo JSON
with open('faturamento.json', 'r') as f:
    dados_faturamento = json.load(f)

# extrai os valores do faturamento diário do mês
faturamento_diario = dados_faturamento['faturamento_diario']

# calcula o menor e o maior faturamento
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# calcula a média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

# exibe os resultados
print('Menor faturamento diário:', menor_faturamento)
print('Maior faturamento diário:', maior_faturamento)
print('Dias com faturamento acima da média mensal:', dias_acima_media)
