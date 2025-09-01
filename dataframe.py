import pandas as pd

base = {
        'Nomes':['Ana', 'Carlos', 'Gabriela', 'Maria'],
        'Fones':[9988774411, 9988774455, 9988774466, 9988778822]
        }

data = pd.DataFrame(base)

print(data)

print(data.dtypes)
