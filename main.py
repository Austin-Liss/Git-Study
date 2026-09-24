import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/Pokemon.csv')

# 1. Which type has the strongest Pokémon?
    # Group by type_1, compute mean total stats. 
    # Then the honest version: some types have 10 Pokémon, some have 100
    # so include counts and ask whether the top type is a real finding or a small-sample artifact.
print(data.columns)

result = data.groupby('Type 1')['Total'].agg(['count', 'mean']).sort_values('mean', ascending=False)
print(result[result['count'] >= 20].sort_values('mean',ascending=False))