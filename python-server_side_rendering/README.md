# Python Server Side Rendering (SSR) with Flask

## 📚 Description

This project demonstrates server-side rendering (SSR) using the Flask web framework in Python. It includes several tasks ranging from generating static HTML from templates to dynamically rendering product data from various sources such as JSON, CSV, and SQLite.

## 🧩 Project Structure

python-server_side_rendering/
├── task_00_generate_invites.py
├── task_01_basic_flask.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── templates/
│ └── product_display.html
├── products.json
├── products.csv
├── products.db
└── README.md

markdown
Copier
Modifier

---

## 🚀 Tasks

### ✅ Task 0: Generate Invitations with Jinja Template

- **File:** `task_00_generate_invites.py`
- **Objective:** Render personalized invitation messages using a Jinja2 template and a list of guest data.
- **Input:** A text template and a list of dictionaries with guest info.
- **Output:** Prints or writes rendered invitation messages for each guest.

---

### ✅ Task 1: Basic Flask App with HTML

- **File:** `task_01_basic_flask.py`
- **Objective:** Render a basic HTML page using Flask and Jinja2.
- **Route:** `/`
- **Template:** Inline or external HTML with a greeting or welcome message.

---

### ✅ Task 2: Display Dynamic List from JSON File

- **File:** `task_02_logic.py`
- **Objective:** Read a list of items from `items.json` and render them in an HTML template.
- **Route:** `/items`
- **Template:** `items.html`
- **Features:** Error handling for missing or invalid JSON.

---

### ✅ Task 3: Display Products from JSON or CSV

- **File:** `task_03_files.py`
- **Route:** `/products?source=[json|csv]&id=<optional>`
- **Objective:**
  - Read product data from `products.json` or `products.csv`.
  - Optionally filter products by `id`.
  - Display data using `product_display.html`.
- **Edge Cases:**
  - Invalid `source` value → shows "Wrong source".
  - Invalid or non-existent `id` → shows "Product not found".
  - Missing data → "No products to display".

---

### ✅ Task 4: Add SQLite Support

- **File:** `task_04_db.py`
- **Database:** `products.db` with `Products` table
- **Objective:**
  - Extend Task 3 to support `source=sql`.
  - Fetch product(s) from SQLite with optional `id`.
  - Render results in `product_display.html`.
- **Setup Script:**
  - Included to create and populate the SQLite DB.
- **Error Handling:**
  - Wrong source.
  - Missing `id`.
  - SQLite errors.

---

## 🖼 Template: `product_display.html`

- Reused across tasks 3 and 4.
- Displays products in a table.
- Handles error and no-data messages with conditional Jinja rendering.

---

## 📦 Requirements

- Python 3.6+
- Flask
- JSON / CSV / SQLite3

```bash
pip install flask
▶️ Usage
Run one of the Flask files and open the route in your browser:

bash
Copier
Modifier
python3 task_03_files.py
# Or
python3 task_04_db.py
Then visit:

http://localhost:5000/products?source=json

http://localhost:5000/products?source=csv

http://localhost:5000/products?source=sql

http://localhost:5000/products?source=json&id=2

🛠 Author
Project done as part of the Holberton School curriculum.