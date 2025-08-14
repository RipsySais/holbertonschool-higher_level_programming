# Python Object-Relational Mapping

This project demonstrates the use of Python with MySQL databases using both MySQLdb and SQLAlchemy ORM.

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files will be executed with MySQLdb version 2.0.x
- Files will be executed with SQLAlchemy version 1.4.x
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation

## Files

### MySQLdb Tasks
- `0-select_states.py` - Lists all states from database
- `1-filter_states.py` - Lists states with name starting with N
- `2-my_filter_states.py` - Filters states by user input
- `3-my_safe_filter_states.py` - Safe filtering (SQL injection protection)
- `4-cities_by_state.py` - Lists all cities with their states
- `5-filter_cities.py` - Lists cities of a specific state

### SQLAlchemy Tasks
- `model_state.py` - State model definition
- `6-model_state.py` - Creates State table
- `7-model_state_fetch_all.py` - Lists all State objects
- `8-model_state_fetch_first.py` - Prints first State object
- `9-model_state_filter_a.py` - Lists states containing letter 'a'
- `10-model_state_my_get.py` - Gets state by name
- `11-model_state_insert.py` - Adds new state
- `12-model_state_update_id_2.py` - Updates state name
- `13-model_state_delete_a.py` - Deletes states with 'a' in name
- `model_city.py` - City model definition
- `14-model_city_fetch_by_state.py` - Lists all City objects

## Usage

Each script can be run with appropriate arguments:
```bash
./script_name.py username password database_name [additional_args]
```

## Author

This project is part of the Holberton School curriculum. 