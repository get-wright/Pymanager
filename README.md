# Pymanager
A Flask-based web application utilizes machine learning to help managers identify which items are purchased together

## Quick start guide
1. Download [Pymanager](https://github.com/get-wright/Pymanager/archive/refs/heads/main.zip) and unzip it.
2. Run the 'Pymanager.bat' to check for missing dependencies. Let the script do it the work for you.  
3. There will be a prompt asking you to access http://127.0.0.1:5000/
4. Upload the '.csv' file contains items bought from the store.

There is a [demo](https://drive.google.com/file/d/1GH25Ta3nKlSzIzbsGxn1y0EZjjbCpSuv/view?usp=sharing) for you to test Pymanager.


## The magic trick

Upon uploading a CSV file, Pymanager processes the file into a pandas DataFrame. It then employs the Eclat algorithm to the data, discovering associations between products.

The Eclat algorithm is a form of association rule learning, a machine learning technique used to uncover interesting relationships between variables in large databases. In this context, it's utilized to identify products that are frequently bought together.

The script then returns the results as a DataFrame, sorted by the support of the associations. The support is a measure of how frequently the items appear together in the dataset.

## Usage for the data provided by Pymanager
Using the provided data, managers can discern which items are frequently purchased together. This insight enables them to effectively utilize the data for:

- **Optimizing store layout**: By strategically placing associated products further apart, customers are encouraged to traverse a longer distance within the store. This increases the likelihood of them purchasing additional items.
- **Tailoring sales to consumer needs**: Understanding purchasing patterns allows for maximization of profits by catering to consumer demands.
- **Efficiently restocking necessary items**: Knowledge of which items are often bought together aids in maintaining optimal inventory levels.

## System Requirement 
It requires a machine running Windows 8.1/Windows 10/Windows 11 (Support for Windows 7 is untested, it may or may not work)

Mac is unsupported (Coming soon)

## Troubleshooting
Please visit 




 
