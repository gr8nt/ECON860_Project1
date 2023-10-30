import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('parsed_files/API_dataset_with_starred_pinned_repo.csv')
df.head()

plt.figure(figsize=(12,4), dpi=200)
sns.scatterplot(x='public_repos', y='followers', data=df)

# plt.xticks(np.arange(0, 600, 150))

plt.xlim(0, 600)
plt.show()
