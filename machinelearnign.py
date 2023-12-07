# -*- coding: utf-8 -*-
"""Machinelearnign.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yZQcVmJJANIvdSyDUoMgXiHyGkx8nBwv
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/new_file.csv")

display(df)

# Drop the column you want to remove
column_to_drop = 'prov'
df.drop(columns=[column_to_drop], inplace=True)

df['LAB_SALARY'] = df['LAB_SALARY'].replace("Not applicable", "0")

# Assuming 'df' is your DataFrame and 'nominal_column' is the column with nominal data
df_encoded = pd.get_dummies(df, columns=['metro'], prefix='nominal')

# Assuming 'df' is your DataFrame and 'nominal_column' is the column with nominal data
df_encoded = pd.get_dummies(df_encoded, columns=['LAB_TRANSP'], prefix='nominal')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Example: Random Forest for predicting a target nominal column
X = df_encoded.drop('LAB_SALARY', axis=1)
y = df_encoded['LAB_SALARY']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Assess model accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")