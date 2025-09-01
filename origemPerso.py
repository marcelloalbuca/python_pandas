import pandas as pd

nomes = ['Ana', 'Carlos', 'Diego', 'Fernando', 'Maria', 'Paulo']

data3 = pd.Series(data = nomes)

print(data3)

indice = [1,2,3,4,5,6]
nomes = ['A','B','C','D','E','F']

data4 = pd.Series(index = indice,
                  data = nomes,
                    )

print(data4)

