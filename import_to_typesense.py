import csv
import typesense

# Configure o cliente Typesense
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',  # Altere se necessário
        'port': '8108',       # Porta padrão do Typesense
        'protocol': 'http'    # Use 'https' se estiver usando SSL
    }],
    'api_key': 'xyz123',         # Substitua pela sua chave de API
    'connection_timeout_seconds': 2
})

# Defina o esquema para a coleção
schema = {
    'name': 'produtos',
    'fields': [
        {'name': 'ID', 'type': 'int32'},  # Adiciona o campo ID
        {'name': 'Nome do Produto', 'type': 'string'},
        {'name': 'Cor', 'type': 'string'},
        {'name': 'Estampa', 'type': 'string'},
        {'name': 'Descrição', 'type': 'string'},
        {'name': 'Palavras-chave', 'type': 'string[]', 'facet': True}
    ],
    'default_sorting_field': 'ID'
}

# Crie a coleção no Typesense
try:
    client.collections.create(schema)
except Exception as e:
    print(f"{e}")

# Leia o CSV e importe os dados
with open('produtos_grande_variedade.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    products = []
    for index, row in enumerate(reader):
        product = {
            'ID': index,  # Adiciona o ID baseado no índice
            'Nome do Produto': row[0],
            'Cor': row[1],
            'Estampa': row[2],
            'Descrição': row[3],
            'Palavras-chave': row[4].split(', ')
        }
        products.append(product)

    # Debug: Imprima o primeiro produto para verificar
    if products:
        print("Primeiro produto lido:", products[0])

    # Indexe os documentos no Typesense
    try:
        response = client.collections['produtos'].documents.import_(products, {'action': 'upsert'})
        print("Resposta da importação:", response)
    except Exception as e:
        print(f"Erro ao importar documentos: {e}")