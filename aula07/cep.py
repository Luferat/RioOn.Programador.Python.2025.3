import requests

def get_address_by_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            return data
        else:
            return {"error": "CEP não encontrado"}
    else:
        return {"error": "Erro na requisição"}

# Exemplo de uso
cep = "23080020"
address = get_address_by_cep(cep)
print(address)
