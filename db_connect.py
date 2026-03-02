import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    "host": "localhost",
    "user": "postgres",
    "password": "postgres123",
    "port": 5432,
}

DATABASE_NAME = "grocery_db"


def create_database():
    conn = psycopg2.connect(database="postgres", **DB_CONFIG)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (DATABASE_NAME,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DATABASE_NAME)))
        print("Database created")
    else:
        print("Database already exists")

    cursor.close()
    conn.close()


def get_connection():
    return psycopg2.connect(database=DATABASE_NAME, **DB_CONFIG)


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            phone VARCHAR(15) UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            price_per_unit DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL CHECK (stock >= 0)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            bill_id SERIAL PRIMARY KEY,
            customer_id INT REFERENCES customers(customer_id),
            product_id INT REFERENCES products(product_id),
            units_bought INT NOT NULL CHECK (units_bought > 0),
            bill_date DATE DEFAULT CURRENT_DATE
        );
    """)

    conn.commit()
    cursor.close()
    print("Tables created")


def run_queries(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print("PostgreSQL version:", version)

    for table in ("customers", "products", "sales"):
        cursor.execute("SELECT COUNT(*) FROM {};".format(table))
        count = cursor.fetchone()[0]
        print("Rows in", table, ":", count)

    cursor.close()


def main():
    create_database()

    conn = get_connection()
    print("Connected to database")

    create_tables(conn)
    run_queries(conn)

    conn.close()
    print("Done")


if __name__ == "__main__":
    main()
