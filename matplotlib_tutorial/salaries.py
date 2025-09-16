import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./salary.csv')
df.drop(['Rating', 'Company Name', 'Location', 'Salaries Reported',
        'Employment Status', 'Job Roles'], axis=1, inplace=True)
avg_salaries = df.groupby('Job Title')['Salary'].mean()
most_paid = avg_salaries.sort_values(ascending=True)
i = 0
for idx, value in most_paid.head(10).items():
  print(f'{idx}: {value}')
  plt.barh(i, value, label=idx)
  i += 1
plt.xlabel('Salary')
plt.title('Most Paid Salaries by Job Title')
plt.legend(loc='lower right')
plt.tight_layout()

plt.show()