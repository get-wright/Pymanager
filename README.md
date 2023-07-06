# Pymanager
A python machine learning model designs to help store managers to identify which items are purchased together.

## Quick start guide
1. Download Pymanager: https://github.com/get-wright/Pymanager/archive/refs/heads/main.zip and unzip it.
2. Run the Pymanager.bat to check for missing dependencies. Let the script do it the work for you.
3. There will be a prompt asking you to access http://127.0.0.1:5000/
4. Upload the .csv file contains items bought from the store.

## The magic

When a CSV file is uploaded, Pymanager reads the file into a pandas DataFrame. It then applies the Apriori algorithm to the data to find associations between products.

The Apriori algorithm is a type of association rule learning, which is a machine learning method for discovering interesting relations between variables in large databases. In this case, it's used to find which products are often purchased together.

The script then returns the results as a DataFrame, sorted by the support of the associations. The support is a measure of how frequently the items appear together in the dataset.


