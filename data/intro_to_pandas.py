from __future__ import print_function

import pandas as pd

pd.__version__

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({'City name': city_names, 'Population': population})

california_housing_dataframe = pd.read_csv(
    "https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()

head = california_housing_dataframe.head()
print(head)

cities = pd.DataFrame({'City name': city_names, 'Population': population})
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:2]))
cities[0:2]
