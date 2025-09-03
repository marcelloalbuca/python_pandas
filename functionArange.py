import pandas as pd
import numpy as np

paises = ['Argentina', 'Brasil', 'Canada', 'Estados Unidos', 'Italia', 'Mexico']

data7 = pd.Series(data = paises, index = np.arange(0,6))

print(data7.index)

print(data7)

