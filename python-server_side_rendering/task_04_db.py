from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_products():
    """Read products from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv_products():
    """Read products from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        return products
    except (FileNotFoundError, csv.Error, ValueError):
        return None

def read_sql_products():
    """Read products from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    elif source == 'sql':
        products = read_sql_products()
    else:
        return render_template('product_display.html', 
                            error="Wrong source. Please use 'json', 'csv', or 'sql'.")
    
    if products is None:
        return render_template('product_display.html', 
                            error=f"Error reading {source} data source.")
    
    if product_id is not None:
        filtered = [p for p in products if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', 
                                error="Product not found")
        products = filtered
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    if not os.path.exists('products.db'):
        import create_db
        create_db.create_database()
    app.run(debug=True, port=5000)
