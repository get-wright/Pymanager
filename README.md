# Pymanager
A python machine learning model designs to help store managers to identify which items are purchased together.

## The magic

When a CSV file is uploaded, Pymanager reads the file into a pandas DataFrame. It then applies the Apriori algorithm to the data to find associations between products.

The Apriori algorithm is a type of association rule learning, which is a machine learning method for discovering interesting relations between variables in large databases. In this case, it's used to find which products are often purchased together.

The script then returns the results as a DataFrame, sorted by the support of the associations. The support is a measure of how frequently the items appear together in the dataset.
