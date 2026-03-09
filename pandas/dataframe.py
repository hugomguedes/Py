import pandas as pd
idades = [
    12,15,62,4,2,55,61,77,5,44,32,52,43,65,33,44
]

nomes = ["ana","maria","roberta","jeremias","carlos","pedro","antonio","antonia","yasmin","pastor","lucas","carvalho","caximbo","francisco","alberto","jonas"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

