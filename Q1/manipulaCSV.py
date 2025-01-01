import csv
import os

# Optei em utilizar essa lib para formatar os valores dos arquivos csv em BRL
from babel.numbers import format_currency 

produtos_dados = []  # Lista para armazenar os dados dos produtos

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'produtos.csv')

# Abrir o arquivo CSV, e o primeiro parâmetro vai depender do nome do arquivo CSV a ser manipulado
with open(csv_path, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    
    # Inicia a busca após o cabeçalho
    next(leitor_csv)
    
    # Iterar pelas linhas restantes
    for linha in leitor_csv:
        produto = linha[0]  # Nome do produto
        quantidade = int(linha[1])  # Quantidade (convertido para inteiro)
        preco = float(linha[2])  # Preço (convertido para float)
        
        # Calcular o valor arrecadado
        valor_arrecadado = quantidade * preco
        
        # Armazenar as informações do produto na lista
        produtos_dados.append((produto, quantidade, preco, round(valor_arrecadado, 2)))
    
# Encontrar o produto com o maior valor arrecadado
produto_maior_valor = max(produtos_dados, key=lambda x: x[3])

# Exibir o produto com o maior valor arrecadado
print(f'\nProduto com o maior lucro: {produto_maior_valor[0]} com valor arrecadado de {format_currency(produto_maior_valor[3], "BRL", locale="pt_BR")}')
