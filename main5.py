def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

entrada = "Exemplo de string"  

resultado = inverter_string(entrada)
print(f"String original: {entrada}")
print(f"String invertida: {resultado}")
