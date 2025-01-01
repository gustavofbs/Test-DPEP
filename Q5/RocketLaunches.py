import requests
import json
import os

def fetch_latest_launch():
    # Solicita ao usuário o ano do lançamento
    year = input("Digite o ano para buscar o último lançamento: ")

    # URL da API com parâmetros para buscar o último lançamento
    url = "https://ll.thespacedevs.com/2.3.0/launches/"
    params = {
        "ordering": "-net",  # Ordenar do mais recente para o mais antigo
        "year": year          # Usar o ano fornecido pelo usuário
    }

    # Caminho completo para o arquivo JSON
    output_path = os.path.join(os.getcwd(), "latest_launch.json")

    # Fazendo a requisição
    response = requests.get(url, params=params)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        if data["results"]:
            launch = data["results"][0]  # Pegando o primeiro (e único) resultado
            
            # Salvando os dados em um arquivo JSON  no caminho que o usuário estiver localizado
            with open(output_path, "w") as file:
                json.dump(launch, file, indent=4)
            
            # Exibindo um resumo no console
            print("\nResumo do lançamento mais recente:")
            print(f"Nome da Missão: {launch['name']}")
            print(f"Data de Lançamento: {launch['net']}")
            print(f"Status: {launch['status']['name']}")
            print(f"Foguete: {launch['rocket']['configuration']['name']}")
            print(f"Local de Lançamento: {launch['pad']['name']}")
            print(f"Dados salvos em: {output_path}")

        else:
            print("Nenhum lançamento encontrado.")
    else:
        print(f"Erro ao acessar a API. Código de status: {response.status_code}")

# Executando a função
fetch_latest_launch()
