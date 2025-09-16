import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
path = os.getcwd() + '/data.csv'

dataframe = pd.read_csv(path)
# Split all languages into a flat list
all_languages = dataframe['LanguagesWorkedWith'].str.split(';').explode()

# Count occurrences and get top 5
top_languages = all_languages.value_counts().head(5)
print(top_languages)
labels = top_languages.index.tolist()
sizes = top_languages.values.tolist()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
plt.title('Most Popular Languages')
plt.tight_layout()
plt.show()
