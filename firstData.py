import pandas as pd
import numpy as np
import tensorflow as tf

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')

y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

print(dftrain.loc[0], y_train.loc[0])
#explanation
dftrain.describe()

dftrain.shape
# Histogram
dftrain.age.hist(bins=20)
dftrain.sex.value_counts().plot(kind = 'barh')
#value_counts = Return a Series containing counts of unique values.
dftrain['class'].value_counts().plot(kind = 'barh') #bar horizontal
pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind = 'barh').set_xlabel('% survived')


categorical_columns = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town', 'alone']
numeric_columns = ['age', 'fare']

feature_columns = []

for feature_name in categorical_columns:
    vocab = dftrain[feature_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocab))

for feature_name in numeric_columns:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval)

linear_est = tf.estimator.LinearClassifier(feature_columns = feature_columns)

linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)

print(result['accuracy'])

prediction = list(linear_est.predict(eval_input_fn))