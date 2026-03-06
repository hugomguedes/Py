import requests

cep = input("entre com o cep ")

url = "https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url.format(cep=cep))

if response.status_code==200:
    print(response.json())