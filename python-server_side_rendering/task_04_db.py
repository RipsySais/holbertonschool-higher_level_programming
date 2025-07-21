#!/usr/bin/env python3
"""
Flask app to display product data from JSON, CSV, or SQLite database
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Path constants
JSON_FILE = 'products.json'
CSV_FILE = 'products.csv'
DB_FILE = 'products.db'


def load_from_json():
    """Load product data from JSON file"""
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        return {"error": f"Failed to load JSON data: {str(e)}"}


def load_from_csv():
    """Load product data from CSV file"""
    try:
        products = []
        with open(CSV_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        return {"error": f"Failed to load CSV data: {str(e)}"}


def load_from_sqlite():
    """Load product data from SQLite database"""
    if not os.path.exists(DB_FILE):
        return {"error": "SQLite database file not found."}
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
        return products
    except Exception as e:
        return {"error": f"Database error: {str(e)}"}


@app.route('/')
def home():
    return '''
        <h2>Welcome to My Product App</h2>
        <ul>
            <li><a href="/products?source=json">View Products (JSON)</a></li>
            <li><a href="/products?source=csv">View Products (CSV)</a></li>
            <li><a href="/products?source=sql">View Products (SQLite)</a></li>
        </ul>
    '''


@app.route('/products')
def display_products():
    """Display products from the selected source"""
    source = request.args.get('source')
    if source == 'json':
        data = load_from_json()
    elif source == 'csv':
        data = load_from_csv()
    elif source == 'sql':
        data = load_from_sqlite()
    else:
        # Affiche un message d'erreur avec code 200
        return render_template("product_display.html", error=f"Source inconnue : {source}", products=None)

    if isinstance(data, dict) and 'error' in data:
        return render_template("product_display.html", error=data['error'], products=None)

    return render_template("product_display.html", products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True)
