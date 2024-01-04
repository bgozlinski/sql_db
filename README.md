# SQL Database Project

## Overview
This project involves the creation and manipulation of a PostgreSQL database using Python. It demonstrates skills in SQL, database schema design, and integrating Python with a SQL database.

## Features
- A PostgreSQL database with tables for students, groups, lecturers, subjects, and grades.
- Python scripts to create database tables, populate them with random data using Faker, and execute complex SQL queries.
- SQL queries for data analysis, including calculating averages, listing data, and aggregating information across different tables.

## Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL
- Python libraries: psycopg2, Faker

### Installation
1. Clone the repository:
```bash
git clone https://github.com/bgozlinski/sql_db.git
```
2. Install the required Python packages:
```bash
pip install -r requirements.txt
```
## Configuration
Before running the scripts, create a `database.ini` file in the project root with the following content:
```
[postgresql]
host=
database=
user=
password=
```

Ensure to replace the above credentials with your actual PostgreSQL database details.

### Usage
1. Update the connection details in `config.py` as per your `database.ini`.
2. Run `create_tables.py` to create the database schema.
3. Use `populate_database.py` to fill the database with random data.
4. Execute SQL queries using the main.py.

## Scripts Description
- `connect.py`: Manages database connections.
- `create_tables.py`: Creates tables in the database.
- `populate_database.py`: Populates the database with random data.
- `queries/`: Contains SQL scripts for data analysis.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
