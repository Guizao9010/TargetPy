dic = {
     1: {"Estado": "SP", "Faturamento": 67836.43},
     2: {"Estado": "RJ", "Faturamento": 36678.66},
     3: {"Estado": "MG", "Faturamento": 29229.88},
     4: {"Estado": "ES", "Faturamento": 27165.48},
     5: {"Estado": "Outros", "Faturamento": 19849.53}
}

total = 0

for i in range (1, 6):
    total += dic[i]["Faturamento"]

print("Percentual de representação de cada estado dentro do faturamento total: ")

for i in range(1, 6):
    per = dic[i]["Faturamento"] / total * 100
    per = round(per, 1)
    n = dic[i]["Estado"]
    print(f"{n}: {per}%")
