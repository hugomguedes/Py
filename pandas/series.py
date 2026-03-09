import pandas as pd 

idades = [
    12,15,62,4,2,55,61,77,5,44,32,52,43,65,33,44
]

seriesIdades = pd.Series(idades)
mediaIdades = seriesIdades.mean()
variancia = seriesIdades.var()
summaryIdades = seriesIdades.describe()

    