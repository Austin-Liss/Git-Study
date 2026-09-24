import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/Pokemon.csv')

# 2. Have Pokémon gotten stronger over generations?
    # Mean total stats by generation. 
    # Then split legendary vs non-legendary — power creep might be entirely explained by more legendaries being added.
    # → groupby on two keys, line plot, unstack or pivot_table
    

result = data.groupby(['Generation','Legendary'])['Total'].agg(['count','mean']).unstack()

means = result['mean']          # Generation × Legendary
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(means.index, means[False], marker='o', label='Non-legendary')
ax.plot(means.index, means[True], marker='s', label='Legendary')

# the overall line, to show what the naive analysis would have told you
overall = data.groupby('Generation')['Total'].mean()
ax.plot(overall.index, overall, marker='^', ls='--', color='gray', label='All Pokémon')

ax.set(title='Base stat total by generation', xlabel='Generation', ylabel='Mean total')
ax.legend(frameon=False)
ax.grid(True, axis='y', alpha=0.3)
ax.set_axisbelow(True)
plt.show()