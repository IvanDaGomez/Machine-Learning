import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('./matplot_fill.csv')
age = df['Age']
all_devs_salaries = df['All_Devs']
python_salaries = df['Python']
js_salaries = df['JavaScript']

plt.plot(age, all_devs_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(age, python_salaries, color='#5a7d9a', label='Python')
plt.fill_between(age, all_devs_salaries, python_salaries,
                where=(all_devs_salaries < python_salaries),
                color='green',
                interpolate=True, label='Above avg',
                alpha=0.25)
plt.fill_between(age, all_devs_salaries, python_salaries,
                where=(all_devs_salaries >= python_salaries),
                interpolate=True, 
                color='red',
                label='Below avg',
                alpha=0.25)
# plt.plot(age, js_salaries, color='#adad3b', label='JavaScript')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.tight_layout()
plt.show()