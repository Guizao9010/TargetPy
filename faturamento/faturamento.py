import json

with open ('dados.json', 'r') as data:
    vetor = json.load(data)

menor = vetor[0]['valor']
maior = vetor[0]['valor']
total = 0
dia = 0
sup = 0

for fat in vetor:
    if fat['valor'] > 0:
        if fat['valor'] < menor:
            menor = fat['valor']
        if fat['valor'] > maior:
            maior = fat['valor']
        total += fat['valor']
        dia += 1

med = total / dia

for fat in vetor:
    if fat['valor'] > med:
        sup += 1

print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maior}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {sup}")
    
    
        

