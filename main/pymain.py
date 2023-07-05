print("██████╗░██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░")
print("██╔══██╗╚██╗░██╔╝████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗")
print("██████╔╝░╚████╔╝░██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝")
print("██╔═══╝░░░╚██╔╝░░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗")
print("██║░░░░░░░░██║░░░██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║")
print("╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝")

print("By tqhe and Luong Ngoc Linh")
print("A python machine learning model designs to help store managers to identify which items are purchased together.")

## Dependencies
import os
import pandas as pd
from apyori import apriori
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

## Creating upload folder for the dataset

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

upload_folder_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
if not os.path.exists(upload_folder_path):
    os.makedirs(upload_folder_path)

@app.route('/', methods=['GET', 'POST'])

# The upload part
def upload():
    if request.method == 'POST' and 'csv_data' in request.files:
        file = request.files['csv_data']
        name = secure_filename(file.name)
        file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], name))
        filepath = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], name)
        asset = pd.read_csv(filepath, header=None)
        
        ## ML model 
        
        if asset.empty:
            print("The dataset is empty.")
        else:
            number_of_rows, number_of_cols = asset.shape
            bill = []
            for i in range(number_of_rows):
                bill.append([str(asset.values[i,j]) for j in range(number_of_cols)])
  
            # Training the Apriori model on the dataset
            rules = apriori(transactions = bill, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

            results = list(rules)
            results

            # Putting the results into a Pandas DataFrame
            
            def inspect(results):
                product_1   = [tuple(result[2][0][0])[0] for result in results]
                product_2   = [tuple(result[2][0][1])[0] for result in results]
                supports    = [result[1] for result in results]
                return list(zip(product_1, product_2, supports))
            resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

            # Sorted by descending supports

            resultsinDataFrame = resultsinDataFrame.sort_values(by='Support', ascending=False)
        return render_template('results.html', results=resultsinDataFrame.to_html(classes='table table-striped'))
    return render_template('upload.html')

