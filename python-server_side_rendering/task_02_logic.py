#!/usr/bin/env python3
"""
Flask app rendering a dynamic list of items from JSON using Jinja
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    """Reads items from a JSON file and renders them in a template."""
    items_list = []
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')

    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except FileNotFoundError:
        app.logger.warning("items.json not found.")
    except json.JSONDecodeError:
        app.logger.error("Invalid JSON format in items.json")

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

