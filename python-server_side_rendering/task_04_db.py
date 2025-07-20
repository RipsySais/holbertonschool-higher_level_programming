#!/usr/bin/env python3
"""
Flask app to display product data from JSON, CSV, or SQLite based on query parameter.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_data(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_data(filepath):
    products = []
    try:
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    products.append(row)
                except ValueError:
                    continue
    except Exception:
        pass
    return products

def read_sqlite_data(db_path, product_id=None):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception:
        return None  # signal an error
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    product_list = []
    error_message = None

    try:
        if id_param:
            product_id = int(id_param)
        else:
            product_id = None
    except ValueError:
        return render_template('product_display.html', error="Invalid ID format")

    # Traitement selon la source
    if source == 'json':
        path = os.path.join(os.path.dirname(__file__), 'products.json')
        product_list = read_json_data(path)
    elif source == 'csv':
        path = os.path.join(os.path.dirname(__file__), 'products.csv')
        product_list = read_csv_data(path)
    elif source == 'sql':
        path = os.path.join(os.path.dirname(__file__), 'products.db')
        product_list = read_sqlite_data(path, product_id)
        if product_list is None:
            error_message = "Database error"
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # Si source != sql, filtrage manuel de l’ID
    if source in ['json', 'csv'] and id_param:
        product_list = [p for p in product_list if int(p.get('id', -1)) == product_id]
        if not product_list:
            error_message = "Product not found"

    return render_template('product_display.html', products=product_list, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
