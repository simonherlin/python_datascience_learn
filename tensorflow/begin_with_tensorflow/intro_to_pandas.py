from __future__ import print_function

import pandas as pd
import numpy as np
"""
    Concepts de base
"""

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()
california_housing_dataframe.head()
california_housing_dataframe.hist('housing_median_age')

"""
    Acceder aux donnees
"""
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:2]))
cities[0:2]

"""
    manipulate data
"""
population / 1000.
np.log(population)
population.apply(lambda val: val > 1000000)

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities
