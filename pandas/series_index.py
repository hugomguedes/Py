import pandas as pd 

idades = [
    12,15,62,4,2,55,61,77,5,44,32,52,43,65,33,44
]

indexs = ["ana","maria","roberta","jeremias","carlos","pedro","antonio","antonia","yasmin","pastor","lucas","carvalho","caximbo","francisco","alberto","jonas"]
# series_idades = pd.Series(idades)
# print(series_idades)

# print(series_idades.iloc[-1])
# print(series_idades.iloc[:3])

series_idades = pd.Series(idades, indexs)
print(series_idades)

## iloc navega nas linhas e loc navega nos indices