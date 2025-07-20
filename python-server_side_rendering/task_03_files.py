#!/usr/bin/env python3
"""
Flask app to display product data from JSON or CSV file using query parameters
"""

from flask import Flask, render_template, request
import json
import csv
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
                # Convert price and id to correct types
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                except ValueError:
                    continue
                products.append(row)
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    product_list = []
    error_message = None

    # Charger les données selon la source
    if source == 'json':
        path = os.path.join(os.path.dirname(__file__), 'products.json')
        product_list = read_json_data(path)
    elif source == 'csv':
        path = os.path.join(os.path.dirname(__file__), 'products.csv')
        product_list = read_csv_data(path)
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # Filtrage par ID si demandé
    if id_param:
        try:
            product_id = int(id_param)
            product_list = [p for p in product_list if int(p.get('id', -1)) == product_id]
            if not product_list:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid ID format"

    return render_template('product_display.html', products=product_list, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
