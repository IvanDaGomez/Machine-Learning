# Intro to pandas and numpy

[Youtube Link](https://www.youtube.com/watch?v=CMEWVn1uZpQ&t=6120)

```python
import os 
import sys
import time
print(sys.platform)             # e.g. 'win32', 'linux', 'darwin'
os.getcwd()                   # Get current working directory
print(os.system('mkdir new_folder'))
print(os.system('ls'))
time.sleep(2)                # Sleep for 2 seconds
print(os.system('rm -r new_folder'))  # Remove the folder created
print(os.system('ls')) 
os.chdir(f'{os.getcwd()}/data')
os.system('echo "name, last_name, date" > hello.txt')              # List files in the current directory
for i in range(100):
  date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  nme = "Ivan"
  last_name = "Gomez"
  os.system(f'echo "{nme}, {last_name}, {date}" >> hello.txt')  # Append to the file
  time.sleep(0.1)
os.system('ls -l hello.txt')  #
os.chdir('..')  # Change back to the parent directory
```

    darwin
    0
    [34mdata[m[m
    intro_to_pandas_and_numpy.ipynb
    [34mnew_folder[m[m
    python_review.ipynb
    0
    0
    [34mdata[m[m
    intro_to_pandas_and_numpy.ipynb
    python_review.ipynb
    0
    -rw-r--r--@ 1 ivandavidgomezsilva  staff  3322 Aug  3 22:26 hello.txt



```python
os.listdir('.')  # List files in the current directory
```




    ['intro_to_pandas_and_numpy.ipynb', 'python_review.ipynb', 'data']




```python
os.makedirs('data/subfolder1/subfolder2', exist_ok=True)  # Create nested directories
```


```python

```

## Pandas

It is a powerful library for data manipulation and analysis, built on top of NumPy.
Clean data, manipulate data, and analyze data.
It is like a spreadsheet in Python.

Advantages of Pandas vs Excel:
- Handles larger datasets efficiently.
- Complex data manipulations are easier.
- Automation and reproducibility with scripts.
- Cross-platform compatibility.

### Pandas terminology

| Excel | Pandas |
|-------|--------|
| Worksheet | DataFrame |
| Column | Series |
| Row heading | Index |
| Row | Row |
| Empty cell | NaN (Not a Number) |

## How to Create a DataFrame

1. With arrays

```python
np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```
- The first row becomes the column names.
- The rest of the rows become the data in the DataFrame.
2. With dictionaries

```python
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
```
- The Keys of the dictionary become the column names.
- The values become the data in the DataFrame.
  
3. With csv files



```python
import pandas as pd
import numpy as np
```


```python
# Option 1: Creating a DataFrame from a NumPy array
array = np.array([['Hello', 'World'], [1, 2], [3.0, 4.0], 
          [True, False], [None, None]])
df = pd.DataFrame(array[1:], columns=array[0])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hello</th>
      <th>World</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Option 2: Creating a DataFrame from a Dictionary
dictionary = {
  'Hello': [1, 3.0, True, None],
  'World': [2, 4.0, False, None]
}
df = pd.DataFrame(dictionary)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hello</th>
      <th>World</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Option 3: Reading from a CSV file
df = pd.read_csv('data/helloWorld.csv')
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hello</th>
      <th>World</th>
      <th>numbers</th>
      <th>boolean</th>
      <th>null</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3.537880</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.012346</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
      <td>41.987654</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.456357</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dtypes
```




    Hello       object
    World       object
    numbers    float64
    boolean       bool
    null       float64
    dtype: object




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>numbers</th>
      <th>null</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>20.248559</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>19.045353</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.537880</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.643729</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.734351</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>33.339181</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>41.987654</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scraping tables from a website
import requests
# Scraping tables from a website
url = 'https://www.britannica.com/topic/list-of-countries-1993160'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
tables = pd.read_html(response.text)
geography_df = tables[0]
geography_df['geographical region'].astype(str) 
geography_df['name'].astype(str)  
geography_df
```

    /var/folders/dh/cyk127ld03gf26jbxvh7s4kc0000gn/T/ipykernel_5192/2888255794.py:7: FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.
      tables = pd.read_html(response.text)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>geographical region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Angola</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Anguilla</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Antigua and Barbuda</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Argentina</td>
      <td>South America</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Armenia</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Aruba</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Australia</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Austria</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Azerbaijan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
geography_df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>geographical region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>Aruba</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Australia</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Austria</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Azerbaijan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
geography_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>geographical region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>Europe</td>
    </tr>
  </tbody>
</table>
</div>




```python
geography_df.shape
```




    (15, 2)



## Attributes, methods, and functions

### 1. Attributes


```python
geography_df.shape
```




    (15, 2)




```python
geography_df.index
```




    RangeIndex(start=0, stop=15, step=1)




```python
geography_df.columns
```




    Index(['name', 'geographical region'], dtype='object')




```python
geography_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>geographical region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Angola</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Anguilla</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Antigua and Barbuda</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Argentina</td>
      <td>South America</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Armenia</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Aruba</td>
      <td>Caribbean</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Australia</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Austria</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Azerbaijan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
geography_df.dtypes
```




    name                   object
    geographical region    object
    dtype: object



### 2. Methods


```python
geography_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>geographical region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>Oceania</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>Europe</td>
    </tr>
  </tbody>
</table>
</div>




```python
geography_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>geographical region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>14</td>
      <td>14</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>14</td>
      <td>6</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Afghanistan</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
geography_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 15 entries, 0 to 14
    Data columns (total 2 columns):
     #   Column               Non-Null Count  Dtype 
    ---  ------               --------------  ----- 
     0   name                 14 non-null     object
     1   geographical region  14 non-null     object
    dtypes: object(2)
    memory usage: 372.0+ bytes


### 3. Functions


```python
len(geography_df)
```




    15




```python
max(geography_df)
```




    'name'




```python
max(geography_df.index)
```




    14




```python
# Rounding values in a DataFrame

df['numbers'] = round(df['numbers'], 2)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hello</th>
      <th>World</th>
      <th>numbers</th>
      <th>boolean</th>
      <th>null</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3.54</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.01</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
      <td>41.99</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.46</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Selecting one column


```python
df['numbers']
```




    0     3.54
    1     5.01
    2    41.99
    3    30.46
    Name: numbers, dtype: float64




```python
df.numbers
```




    0     3.54
    1     5.01
    2    41.99
    3    30.46
    Name: numbers, dtype: float64



### Sample with a large dataset


```python
airlines_df = pd.read_csv('data/airlines_flights_data.csv')
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>SpiceJet</td>
      <td>SG-8709</td>
      <td>Delhi</td>
      <td>Evening</td>
      <td>zero</td>
      <td>Night</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5953</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>SpiceJet</td>
      <td>SG-8157</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5953</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>AirAsia</td>
      <td>I5-764</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Early_Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5956</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Vistara</td>
      <td>UK-995</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.25</td>
      <td>1</td>
      <td>5955</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Vistara</td>
      <td>UK-963</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5955</td>
    </tr>
  </tbody>
</table>
</div>




```python
airlines_df.shape
```




    (300153, 12)




```python
airlines_df[['flight', 'departure_time']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>flight</th>
      <th>departure_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SG-8709</td>
      <td>Evening</td>
    </tr>
    <tr>
      <th>1</th>
      <td>SG-8157</td>
      <td>Early_Morning</td>
    </tr>
    <tr>
      <th>2</th>
      <td>I5-764</td>
      <td>Early_Morning</td>
    </tr>
    <tr>
      <th>3</th>
      <td>UK-995</td>
      <td>Morning</td>
    </tr>
    <tr>
      <th>4</th>
      <td>UK-963</td>
      <td>Morning</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>300148</th>
      <td>UK-822</td>
      <td>Morning</td>
    </tr>
    <tr>
      <th>300149</th>
      <td>UK-826</td>
      <td>Afternoon</td>
    </tr>
    <tr>
      <th>300150</th>
      <td>UK-832</td>
      <td>Early_Morning</td>
    </tr>
    <tr>
      <th>300151</th>
      <td>UK-828</td>
      <td>Early_Morning</td>
    </tr>
    <tr>
      <th>300152</th>
      <td>UK-822</td>
      <td>Morning</td>
    </tr>
  </tbody>
</table>
<p>300153 rows × 2 columns</p>
</div>




```python
airlines_df.columns
```




    Index(['index', 'airline', 'flight', 'source_city', 'departure_time', 'stops',
           'arrival_time', 'destination_city', 'class', 'duration', 'days_left',
           'price'],
          dtype='object')




```python
airlines_df.dtypes
```




    index                 int64
    airline              object
    flight               object
    source_city          object
    departure_time       object
    stops                object
    arrival_time         object
    destination_city     object
    class                object
    duration            float64
    days_left             int64
    price                 int64
    dtype: object




```python
airlines_df['price_per_minute'] = airlines_df['price'] / (airlines_df['duration'] * 60)
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>SpiceJet</td>
      <td>SG-8709</td>
      <td>Delhi</td>
      <td>Evening</td>
      <td>zero</td>
      <td>Night</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5953</td>
      <td>45.721966</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>SpiceJet</td>
      <td>SG-8157</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5953</td>
      <td>42.582260</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>AirAsia</td>
      <td>I5-764</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Early_Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5956</td>
      <td>45.745008</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Vistara</td>
      <td>UK-995</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.25</td>
      <td>1</td>
      <td>5955</td>
      <td>44.111111</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Vistara</td>
      <td>UK-963</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5955</td>
      <td>42.596567</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.random.seed(42) # the universal response to everything
airlines_df['random_values'] = np.random.randint(1, 100, size=len(airlines_df))
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>SpiceJet</td>
      <td>SG-8709</td>
      <td>Delhi</td>
      <td>Evening</td>
      <td>zero</td>
      <td>Night</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5953</td>
      <td>45.721966</td>
      <td>52</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>SpiceJet</td>
      <td>SG-8157</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5953</td>
      <td>42.582260</td>
      <td>93</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>AirAsia</td>
      <td>I5-764</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Early_Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5956</td>
      <td>45.745008</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Vistara</td>
      <td>UK-995</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.25</td>
      <td>1</td>
      <td>5955</td>
      <td>44.111111</td>
      <td>72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Vistara</td>
      <td>UK-963</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5955</td>
      <td>42.596567</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>



### Adding using the assign method


```python
score1 = np.random.randint(1, 100, size=len(airlines_df))
score2 = np.random.randint(1, 100, size=len(airlines_df))

series1 = pd.Series(score1, name='score1')
series2 = pd.Series(score2, name='score2')
# Assign method allows to add multiple columns at once
airlines_df = airlines_df.assign(score1=series1, score2=series2)
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>SpiceJet</td>
      <td>SG-8709</td>
      <td>Delhi</td>
      <td>Evening</td>
      <td>zero</td>
      <td>Night</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5953</td>
      <td>45.721966</td>
      <td>52</td>
      <td>15</td>
      <td>51</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>SpiceJet</td>
      <td>SG-8157</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5953</td>
      <td>42.582260</td>
      <td>93</td>
      <td>78</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>AirAsia</td>
      <td>I5-764</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Early_Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5956</td>
      <td>45.745008</td>
      <td>15</td>
      <td>91</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Vistara</td>
      <td>UK-995</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.25</td>
      <td>1</td>
      <td>5955</td>
      <td>44.111111</td>
      <td>72</td>
      <td>39</td>
      <td>84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Vistara</td>
      <td>UK-963</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5955</td>
      <td>42.596567</td>
      <td>61</td>
      <td>95</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
</div>



### Using insert method




```python
airlines_df.insert(0, 'other_new_column', np.random.randint(1, 100, size=len(airlines_df)))
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>64</td>
      <td>0</td>
      <td>SpiceJet</td>
      <td>SG-8709</td>
      <td>Delhi</td>
      <td>Evening</td>
      <td>zero</td>
      <td>Night</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5953</td>
      <td>45.721966</td>
      <td>52</td>
      <td>15</td>
      <td>51</td>
    </tr>
    <tr>
      <th>1</th>
      <td>61</td>
      <td>1</td>
      <td>SpiceJet</td>
      <td>SG-8157</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5953</td>
      <td>42.582260</td>
      <td>93</td>
      <td>78</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>66</td>
      <td>2</td>
      <td>AirAsia</td>
      <td>I5-764</td>
      <td>Delhi</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Early_Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.17</td>
      <td>1</td>
      <td>5956</td>
      <td>45.745008</td>
      <td>15</td>
      <td>91</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16</td>
      <td>3</td>
      <td>Vistara</td>
      <td>UK-995</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.25</td>
      <td>1</td>
      <td>5955</td>
      <td>44.111111</td>
      <td>72</td>
      <td>39</td>
      <td>84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>78</td>
      <td>4</td>
      <td>Vistara</td>
      <td>UK-963</td>
      <td>Delhi</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Mumbai</td>
      <td>Economy</td>
      <td>2.33</td>
      <td>1</td>
      <td>5955</td>
      <td>42.596567</td>
      <td>61</td>
      <td>95</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
</div>



## Math Operations


```python
airlines_df['duration'].sum()
```




    np.float64(3668176.0599999996)




```python
airlines_df['duration'].mean()
```




    np.float64(12.221020812718846)




```python
airlines_df['duration'].median()
```




    11.25




```python
airlines_df['duration'].std()
```




    7.191997238118316




```python
airlines_df['duration'].mean()
```




    np.float64(12.221020812718846)




```python
airlines_df['calculation_result'] = airlines_df['duration'] * airlines_df['price_per_minute']
airlines_df.insert(0, 'scaled', (airlines_df['calculation_result'] - airlines_df['calculation_result'].mean()) / airlines_df['calculation_result'].std())
airlines_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3.001530e+05</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
      <td>300153.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-2.121073e-17</td>
      <td>50.063324</td>
      <td>150076.000000</td>
      <td>12.221021</td>
      <td>26.004751</td>
      <td>20889.660523</td>
      <td>36.257713</td>
      <td>49.962959</td>
      <td>49.923312</td>
      <td>49.999490</td>
      <td>348.161009</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.000000e+00</td>
      <td>28.582024</td>
      <td>86646.852011</td>
      <td>7.191997</td>
      <td>13.561004</td>
      <td>22697.767366</td>
      <td>45.557214</td>
      <td>28.599023</td>
      <td>28.593038</td>
      <td>28.596999</td>
      <td>378.296123</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-8.716567e-01</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.830000</td>
      <td>1.000000</td>
      <td>1105.000000</td>
      <td>1.724114</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-7.096143e-01</td>
      <td>25.000000</td>
      <td>75038.000000</td>
      <td>6.830000</td>
      <td>15.000000</td>
      <td>4783.000000</td>
      <td>7.669630</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>79.716667</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-5.932152e-01</td>
      <td>50.000000</td>
      <td>150076.000000</td>
      <td>11.250000</td>
      <td>26.000000</td>
      <td>7425.000000</td>
      <td>16.304348</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>123.750000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9.530162e-01</td>
      <td>75.000000</td>
      <td>225114.000000</td>
      <td>16.170000</td>
      <td>38.000000</td>
      <td>42521.000000</td>
      <td>48.214376</td>
      <td>75.000000</td>
      <td>75.000000</td>
      <td>75.000000</td>
      <td>708.683333</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.501823e+00</td>
      <td>99.000000</td>
      <td>300152.000000</td>
      <td>49.830000</td>
      <td>49.000000</td>
      <td>123071.000000</td>
      <td>474.551282</td>
      <td>99.000000</td>
      <td>99.000000</td>
      <td>99.000000</td>
      <td>2051.183333</td>
    </tr>
  </tbody>
</table>
</div>



### Value counts method


```python
airlines_df['duration'].count() == len(airlines_df['duration'])
```




    np.True_




```python
airlines_df['duration'].value_counts()
```




    duration
    2.17     4242
    2.25     4036
    2.75     2879
    2.08     2755
    2.83     2323
             ... 
    37.17       1
    38.75       1
    38.50       1
    36.25       1
    41.50       1
    Name: count, Length: 476, dtype: int64




```python
# By percentage
(airlines_df['duration'].value_counts(normalize=True) * 100).round(5).astype(str) + ' %'
```




    duration
    2.17     1.41328 %
    2.25     1.34465 %
    2.75     0.95918 %
    2.08     0.91787 %
    2.83     0.77394 %
               ...    
    37.17    0.00033 %
    38.75    0.00033 %
    38.50    0.00033 %
    36.25    0.00033 %
    41.50    0.00033 %
    Name: proportion, Length: 476, dtype: object



### Sort a dataframe


```python
airlines_df.sort_values('duration').head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>118982</th>
      <td>-0.849672</td>
      <td>96</td>
      <td>118982</td>
      <td>Indigo</td>
      <td>6E-357</td>
      <td>Bangalore</td>
      <td>Night</td>
      <td>zero</td>
      <td>Night</td>
      <td>Chennai</td>
      <td>Economy</td>
      <td>0.83</td>
      <td>42</td>
      <td>1604</td>
      <td>32.208835</td>
      <td>98</td>
      <td>72</td>
      <td>17</td>
      <td>26.733333</td>
    </tr>
    <tr>
      <th>118622</th>
      <td>-0.849672</td>
      <td>19</td>
      <td>118622</td>
      <td>Indigo</td>
      <td>6E-357</td>
      <td>Bangalore</td>
      <td>Night</td>
      <td>zero</td>
      <td>Night</td>
      <td>Chennai</td>
      <td>Economy</td>
      <td>0.83</td>
      <td>38</td>
      <td>1604</td>
      <td>32.208835</td>
      <td>20</td>
      <td>73</td>
      <td>98</td>
      <td>26.733333</td>
    </tr>
    <tr>
      <th>197626</th>
      <td>-0.856765</td>
      <td>49</td>
      <td>197626</td>
      <td>Indigo</td>
      <td>6E-987</td>
      <td>Chennai</td>
      <td>Early_Morning</td>
      <td>zero</td>
      <td>Early_Morning</td>
      <td>Bangalore</td>
      <td>Economy</td>
      <td>0.83</td>
      <td>48</td>
      <td>1443</td>
      <td>28.975904</td>
      <td>3</td>
      <td>24</td>
      <td>20</td>
      <td>24.050000</td>
    </tr>
    <tr>
      <th>116322</th>
      <td>-0.766228</td>
      <td>26</td>
      <td>116322</td>
      <td>Indigo</td>
      <td>6E-357</td>
      <td>Bangalore</td>
      <td>Night</td>
      <td>zero</td>
      <td>Night</td>
      <td>Chennai</td>
      <td>Economy</td>
      <td>0.83</td>
      <td>12</td>
      <td>3498</td>
      <td>70.240964</td>
      <td>59</td>
      <td>52</td>
      <td>89</td>
      <td>58.300000</td>
    </tr>
    <tr>
      <th>197628</th>
      <td>-0.856765</td>
      <td>7</td>
      <td>197628</td>
      <td>Indigo</td>
      <td>6E-6137</td>
      <td>Chennai</td>
      <td>Morning</td>
      <td>zero</td>
      <td>Morning</td>
      <td>Bangalore</td>
      <td>Economy</td>
      <td>0.83</td>
      <td>48</td>
      <td>1443</td>
      <td>28.975904</td>
      <td>59</td>
      <td>15</td>
      <td>23</td>
      <td>24.050000</td>
    </tr>
  </tbody>
</table>
</div>




```python
airlines_df = airlines_df.sort_values(['price', 'duration'], ascending=True).reset_index(drop=True)
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.871657</td>
      <td>35</td>
      <td>206273</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>45</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>85</td>
      <td>82</td>
      <td>18</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.871657</td>
      <td>36</td>
      <td>206352</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>46</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>49</td>
      <td>1</td>
      <td>61</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.871657</td>
      <td>4</td>
      <td>206432</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>47</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>2</td>
      <td>18</td>
      <td>45</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.871657</td>
      <td>63</td>
      <td>206509</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>48</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>15</td>
      <td>69</td>
      <td>50</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.871657</td>
      <td>64</td>
      <td>206589</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>49</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>25</td>
      <td>72</td>
      <td>70</td>
      <td>18.416667</td>
    </tr>
  </tbody>
</table>
</div>



### Create indexes


```python
new_index = np.arange(0, len(airlines_df))
new_index
```




    array([     0,      1,      2, ..., 300150, 300151, 300152])




```python
import random
random.seed(42)
random.shuffle(new_index)
```


```python
airlines_df['new_index'] = new_index
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
      <th>new_index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.871657</td>
      <td>35</td>
      <td>206273</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>45</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>85</td>
      <td>82</td>
      <td>18</td>
      <td>18.416667</td>
      <td>153245</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.871657</td>
      <td>36</td>
      <td>206352</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>46</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>49</td>
      <td>1</td>
      <td>61</td>
      <td>18.416667</td>
      <td>187668</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.871657</td>
      <td>4</td>
      <td>206432</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>47</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>2</td>
      <td>18</td>
      <td>45</td>
      <td>18.416667</td>
      <td>66094</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.871657</td>
      <td>63</td>
      <td>206509</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>48</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>15</td>
      <td>69</td>
      <td>50</td>
      <td>18.416667</td>
      <td>163598</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.871657</td>
      <td>64</td>
      <td>206589</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>49</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>25</td>
      <td>72</td>
      <td>70</td>
      <td>18.416667</td>
      <td>259375</td>
    </tr>
  </tbody>
</table>
</div>




```python
# renaming with column
airlines_df['duration'].rename('flight_duration', inplace=True)
airlines_df.head()  
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
      <th>new_index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.871657</td>
      <td>35</td>
      <td>206273</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>45</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>85</td>
      <td>82</td>
      <td>18</td>
      <td>18.416667</td>
      <td>153245</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.871657</td>
      <td>36</td>
      <td>206352</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>46</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>49</td>
      <td>1</td>
      <td>61</td>
      <td>18.416667</td>
      <td>187668</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.871657</td>
      <td>4</td>
      <td>206432</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>47</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>2</td>
      <td>18</td>
      <td>45</td>
      <td>18.416667</td>
      <td>66094</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.871657</td>
      <td>63</td>
      <td>206509</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>48</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>15</td>
      <td>69</td>
      <td>50</td>
      <td>18.416667</td>
      <td>163598</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.871657</td>
      <td>64</td>
      <td>206589</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>49</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>25</td>
      <td>72</td>
      <td>70</td>
      <td>18.416667</td>
      <td>259375</td>
    </tr>
  </tbody>
</table>
</div>




```python
# set the new index
airlines_df.set_index('new_index', inplace=True)
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
    </tr>
    <tr>
      <th>new_index</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>153245</th>
      <td>-0.871657</td>
      <td>35</td>
      <td>206273</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>45</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>85</td>
      <td>82</td>
      <td>18</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>187668</th>
      <td>-0.871657</td>
      <td>36</td>
      <td>206352</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>46</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>49</td>
      <td>1</td>
      <td>61</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>66094</th>
      <td>-0.871657</td>
      <td>4</td>
      <td>206432</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>47</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>2</td>
      <td>18</td>
      <td>45</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>163598</th>
      <td>-0.871657</td>
      <td>63</td>
      <td>206509</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>48</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>15</td>
      <td>69</td>
      <td>50</td>
      <td>18.416667</td>
    </tr>
    <tr>
      <th>259375</th>
      <td>-0.871657</td>
      <td>64</td>
      <td>206589</td>
      <td>GO_FIRST</td>
      <td>G8-504</td>
      <td>Chennai</td>
      <td>Afternoon</td>
      <td>zero</td>
      <td>Afternoon</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>1.0</td>
      <td>49</td>
      <td>1105</td>
      <td>18.416667</td>
      <td>25</td>
      <td>72</td>
      <td>70</td>
      <td>18.416667</td>
    </tr>
  </tbody>
</table>
</div>




```python
airlines_df.sort_index(inplace=True)
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>other_new_column</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>price_per_minute</th>
      <th>random_values</th>
      <th>score1</th>
      <th>score2</th>
      <th>calculation_result</th>
    </tr>
    <tr>
      <th>new_index</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.747812</td>
      <td>41</td>
      <td>74412</td>
      <td>GO_FIRST</td>
      <td>G8-319</td>
      <td>Mumbai</td>
      <td>Morning</td>
      <td>one</td>
      <td>Night</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>11.92</td>
      <td>30</td>
      <td>3916</td>
      <td>5.475391</td>
      <td>73</td>
      <td>82</td>
      <td>79</td>
      <td>65.266667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.469062</td>
      <td>67</td>
      <td>126334</td>
      <td>Vistara</td>
      <td>UK-772</td>
      <td>Kolkata</td>
      <td>Morning</td>
      <td>one</td>
      <td>Night</td>
      <td>Delhi</td>
      <td>Economy</td>
      <td>11.17</td>
      <td>42</td>
      <td>10243</td>
      <td>15.283497</td>
      <td>29</td>
      <td>55</td>
      <td>78</td>
      <td>170.716667</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.750191</td>
      <td>18</td>
      <td>138181</td>
      <td>AirAsia</td>
      <td>I5-547</td>
      <td>Kolkata</td>
      <td>Evening</td>
      <td>one</td>
      <td>Afternoon</td>
      <td>Bangalore</td>
      <td>Economy</td>
      <td>16.42</td>
      <td>21</td>
      <td>3862</td>
      <td>3.920016</td>
      <td>83</td>
      <td>26</td>
      <td>98</td>
      <td>64.366667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.586210</td>
      <td>33</td>
      <td>70523</td>
      <td>Air_India</td>
      <td>AI-809</td>
      <td>Mumbai</td>
      <td>Morning</td>
      <td>one</td>
      <td>Morning</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>24.50</td>
      <td>3</td>
      <td>7584</td>
      <td>5.159184</td>
      <td>1</td>
      <td>39</td>
      <td>56</td>
      <td>126.400000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.896457</td>
      <td>77</td>
      <td>270606</td>
      <td>Vistara</td>
      <td>UK-778</td>
      <td>Kolkata</td>
      <td>Afternoon</td>
      <td>one</td>
      <td>Night</td>
      <td>Hyderabad</td>
      <td>Business</td>
      <td>7.58</td>
      <td>9</td>
      <td>63935</td>
      <td>140.578276</td>
      <td>12</td>
      <td>43</td>
      <td>64</td>
      <td>1065.583333</td>
    </tr>
  </tbody>
</table>
</div>




```python
airlines_df = airlines_df.rename(columns={
  'flight_duration': 'duration',
  'other_new_column': 'OTC',
  'price_per_minute': 'PPM',
  'score1': 'S1',
  'score2': 'S2'
  }) 
# Renaming with dictionary
```


```python
# show df
airlines_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scaled</th>
      <th>OTC</th>
      <th>index</th>
      <th>airline</th>
      <th>flight</th>
      <th>source_city</th>
      <th>departure_time</th>
      <th>stops</th>
      <th>arrival_time</th>
      <th>destination_city</th>
      <th>class</th>
      <th>duration</th>
      <th>days_left</th>
      <th>price</th>
      <th>PPM</th>
      <th>random_values</th>
      <th>S1</th>
      <th>S2</th>
      <th>calculation_result</th>
    </tr>
    <tr>
      <th>new_index</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.747812</td>
      <td>41</td>
      <td>74412</td>
      <td>GO_FIRST</td>
      <td>G8-319</td>
      <td>Mumbai</td>
      <td>Morning</td>
      <td>one</td>
      <td>Night</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>11.92</td>
      <td>30</td>
      <td>3916</td>
      <td>5.475391</td>
      <td>73</td>
      <td>82</td>
      <td>79</td>
      <td>65.266667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.469062</td>
      <td>67</td>
      <td>126334</td>
      <td>Vistara</td>
      <td>UK-772</td>
      <td>Kolkata</td>
      <td>Morning</td>
      <td>one</td>
      <td>Night</td>
      <td>Delhi</td>
      <td>Economy</td>
      <td>11.17</td>
      <td>42</td>
      <td>10243</td>
      <td>15.283497</td>
      <td>29</td>
      <td>55</td>
      <td>78</td>
      <td>170.716667</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.750191</td>
      <td>18</td>
      <td>138181</td>
      <td>AirAsia</td>
      <td>I5-547</td>
      <td>Kolkata</td>
      <td>Evening</td>
      <td>one</td>
      <td>Afternoon</td>
      <td>Bangalore</td>
      <td>Economy</td>
      <td>16.42</td>
      <td>21</td>
      <td>3862</td>
      <td>3.920016</td>
      <td>83</td>
      <td>26</td>
      <td>98</td>
      <td>64.366667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.586210</td>
      <td>33</td>
      <td>70523</td>
      <td>Air_India</td>
      <td>AI-809</td>
      <td>Mumbai</td>
      <td>Morning</td>
      <td>one</td>
      <td>Morning</td>
      <td>Hyderabad</td>
      <td>Economy</td>
      <td>24.50</td>
      <td>3</td>
      <td>7584</td>
      <td>5.159184</td>
      <td>1</td>
      <td>39</td>
      <td>56</td>
      <td>126.400000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.896457</td>
      <td>77</td>
      <td>270606</td>
      <td>Vistara</td>
      <td>UK-778</td>
      <td>Kolkata</td>
      <td>Afternoon</td>
      <td>one</td>
      <td>Night</td>
      <td>Hyderabad</td>
      <td>Business</td>
      <td>7.58</td>
      <td>9</td>
      <td>63935</td>
      <td>140.578276</td>
      <td>12</td>
      <td>43</td>
      <td>64</td>
      <td>1065.583333</td>
    </tr>
  </tbody>
</table>
</div>


