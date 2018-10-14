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
