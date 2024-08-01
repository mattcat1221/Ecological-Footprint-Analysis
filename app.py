import sqlite3, pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1.0/ecological_data')
def data():
    
    people_df = pd.read_sql_table('people', 'sqlite:///ecological_db')
    land_df = pd.read_sql_table('land', 'sqlite:///ecological_db')
    
    df = people_df.merge(land_df)
    
    return df.to_dict(orient='records')