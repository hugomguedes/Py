import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

def str_to_float(x:str):
    x=float(x.replace(" ", "").replace(",", ".").replace("\xa0", ""))
    return x

def exp_to_anos(exp:str):
    return float(exp.replace(",",".").replace("anos",""))

if response.status_code == 200:
    dfs = pd.read_html(response.text)
    uf = dfs[1]

    uf["Área (km²)"] =uf["Área (km²)"].apply(str_to_float)
    uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
    uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

    print(uf["Área (km²)"])
    print(uf["PIB (2015)"])
    print(uf["Expectativa de vida (2016)"])



