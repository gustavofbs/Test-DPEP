def analisar_numeros(numeros):
    if not numeros:
        return {
            "media": None,
            "maior": None,
            "menor": None,
            "pares": 0
        }

    # optei em já retornar com os valores calculados, mas também poderia ter feito isso antes
    return {
        "media": sum(numeros) / len(numeros),
        "maior": max(numeros),
        "menor": min(numeros),
        "pares": sum(1 for num in numeros if num % 2 == 0)
    }


# Testes
if __name__ == "__main__":
    # Teste 1: Lista com números positivos
    numeros = [10, 19, 20, 29, 30]
    resultado = analisar_numeros(numeros)
    print("Teste 1:", resultado) 
    # Resultado: Teste 1: {'media': 21.6, 'maior': 30, 'menor': 10, 'pares': 3}

    # Teste 2: Lista com números negativos e positivos
    numeros = [-10, -19, 20, 29, 30]
    resultado = analisar_numeros(numeros)
    print("Teste 2:", resultado)
    # Resultado: Teste 2: {'media': 10.0, 'maior': 30, 'menor': -19, 'pares': 3}

    # Teste 3: Lista com apenas um número
    numeros = [5]
    resultado = analisar_numeros(numeros)
    print("Teste 3:", resultado) 
    # Resultado: Teste 3: {'media': 5.0, 'maior': 5, 'menor': 5, 'pares': 0}

    # Teste 4: Lista vazia
    numeros = []
    resultado = analisar_numeros(numeros)
    print("Teste 4:", resultado) 
    # Resultado: Teste 4: {'media': None, 'maior': None, 'menor': None, 'pares': 0}

    # Teste 5: Lista com números pares e ímpares
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = analisar_numeros(numeros)
    print("Teste 5:", resultado) 
    # Resultado: Teste 5: {'media': 5.5, 'maior': 10, 'menor': 1, 'pares': 5}