from __future__ import print_function

import pandas as pd

"""
    Concepts de base
     On distingue deux grandes catégories de structures de données Pandas :

    Le DataFrame, un tableau relationnel de données, avec des lignes et des colonnes étiquetées
    La Series, constituée d'une seule colonne. Un DataFrame contient une ou plusieurs Series, chacune étant étiquetée.

    Le DataFrame est une abstraction fréquemment utilisée pour manipuler des données. Spark et R proposent des implémentations similaires.

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
    Accéder aux données
    L'accès aux données d'un DataFrame s'effectue au moyen d'opérations de liste ou de dictionnaire Python courantes
"""
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:2]))
cities[0:2]
