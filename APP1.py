from flask import Flask, render_template, send_file, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

app = Flask(__name__)

# Load the data into a DataFrame with different encodings
data_file = 'Resources/Global Ecological Footprint 2023.csv'
encodings = ['utf-8', 'ISO-8859-1', 'cp1252', 'utf-16']

df = None
for enc in encodings:
    try:
        df = pd.read_csv(data_file, encoding=enc)
        print(f"File successfully read with encoding: {enc}")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to read with encoding {enc}: {e}")

if df is None:
    raise ValueError("None of the specified encodings could read the file.")

# Load the data into a DataFrame (assuming a CSV file)
data_file = 'Resources/Global Ecological Footprint 2023.csv'
df = pd.read_csv(data_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(df.to_dict(orient='records'))

@app.route('/plot')
def plot():
    # Generate a plot
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Per Capita GDP'].dropna(), kde=True, bins=30)
    plt.title('Distribution of Per Capita GDP')
    plt.xlabel('Per Capita GDP')
    plt.ylabel('Frequency')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/download_ppt')
def download_ppt():
    return send_file('/Users/cmatthews/Desktop/Data-Analyst/2023 Ecological Analysis Powerpoint.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
