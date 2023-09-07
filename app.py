from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your data into a pandas DataFrame
# Replace 'your_data.csv' with the actual path to your data file
data = pd.read_csv('info.csv')

@app.route('/get_loan_message', methods=['GET'])
def get_loan_message():
    index_number = request.args.get('index_number')

    if index_number is None:
        return jsonify({'error': 'Index number parameter is missing'}), 400

    # Search for the row with the given INDEXNO
    row = data[data['INDEXNO'] == index_number]

    if row.empty:
        return jsonify({'error': 'Index number not found'}), 404

    loan_message = row.iloc[0]['Loan_message']
    return jsonify({'Loan_message': loan_message})

if __name__ == '__main__':
    app.run()



