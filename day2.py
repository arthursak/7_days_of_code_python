import requests
from googletrans import Translator

#Otimiza o uso da função de tradução
translator = Translator()

#URL para onde será enviada a requisição
url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Envia o request para a requisição
response = requests.get(url)

# Se retorna 200, OK. Se não BO
if response.status_code == 200:
    
    dados = response.json()
    print("Dados do request:", dados)

    # Traduzindo name
    for character in dados:
        if "name" in character:
            translated_name = translator.translate(character["name"], dest="pt").text
            print(f"Original: {character["name"]} | Traduzido: {translated_name}")

    # Traduzindo affiliation
    for character in dados:
        if "affiliation" in character:
            translated_affili = translator.translate(character["affiliation"], dest="pt").text
            print(f"Original: {character["affiliation"]} | Traduzido: {translated_affili}")

else:
    print(f"Erro na requisição. Status code: {response.status_code}")