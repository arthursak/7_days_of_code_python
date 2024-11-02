import requests

#URL para onde será enviada a requisição
url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Envia o request para a requisição
response = requests.get(url)

# Se retorna 200, OK. Se não BO
if response.status_code == 200:
    
    dados = response.json()
    print("Dados do request:", dados)
else:
    print(f"Erro na requisição. Status code: {response.status_code}")