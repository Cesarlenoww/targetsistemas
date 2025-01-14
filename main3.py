import json

def calcular_faturamento():
    with open('faturamento.json') as file:
        dados = json.load(file)
    
    faturamento_diario = dados["faturamento"]

    dias_com_faturamento = [valor for valor in faturamento_diario if valor is not None]
    
    if not dias_com_faturamento:
        print("Não há dados de faturamento disponíveis.")
        return
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    
    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    
    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

calcular_faturamento()