import requests
import json
import pandas as pd
from tqdm import tqdm 
ceps = ["01001000",
        "20040020",
        "30130100",
        "70040010",
        "40010010",
        "60060100",
        "90010150"]
url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    response = requests.get(url.format(cep=i))

    if response.status_code ==200:
        dados.append(response.json())

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv",sep=";") # criando arquivo dataset csv


with open("ceps.json", "w", encoding="utf-8") as openFile:
    json.dump(dados, openFile, ensure_ascii=False, indent=4)