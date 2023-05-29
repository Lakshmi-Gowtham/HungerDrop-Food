import unittest
import sqlite3

class TestOrdersTable(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE orders (
                id INTEGER NOT NULL,
                name VARCHAR(200) NOT NULL,
                lname VARCHAR(200) NOT NULL,
                company_name VARCHAR(200) NOT NULL,
                address VARCHAR(200) NOT NULL,
                city VARCHAR(200) NOT NULL,
                country VARCHAR(200) NOT NULL,
                zip_code INTEGER(20) NOT NULL,
                email VARCHAR(200) NOT NULL,
                phone_number INTEGER(20) NOT NULL,
                order_notes TEXT NOT NULL,
                status VARCHAR(200) NOT NULL DEFAULT 'sent to admins',
                price INTEGER(20) NOT NULL,
                user_id INTEGER(10) NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (id)
            )
        ''')

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_table_exists(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_columns_exist(self):
        self.cursor.execute("PRAGMA table_info('orders')")
        columns = self.cursor.fetchall()

        expected_columns = [
            ('id', 'INTEGER'),
            ('name', 'VARCHAR(200)'),
            ('lname', 'VARCHAR(200)'),
            ('company_name', 'VARCHAR(200)'),
            ('address', 'VARCHAR(200)'),
            ('city', 'VARCHAR(200)'),
            ('country', 'VARCHAR(200)'),
            ('zip_code', 'INTEGER(20)'),
            ('email', 'VARCHAR(200)'),
            ('phone_number', 'INTEGER(20)'),
            ('order_notes', 'TEXT'),
            ('status', 'VARCHAR(200)'),
            ('price', 'INTEGER(20)'),
            ('user_id', 'INTEGER(10)'),
            ('created_at', 'TIMESTAMP')
        ]

        actual_columns = [(column[1], column[2]) for column in columns]

        self.assertCountEqual(actual_columns, expected_columns)


    def test_default_status(self):
        self.cursor.execute("""
            INSERT INTO orders (id, name, lname, company_name, address, city, country, zip_code, email, phone_number, order_notes, price, user_id)
            VALUES 
            (1, 'Lakshmi', 'Gowtham', 'HungerDrop', '123 Main St', 'City', 'Country', 12345, 'john@example.com', 1234567890, 'Some notes', 50, 1),
            (2, 'Kunal', 'Raj', 'Company', '456 Elm St', 'City', 'Country', 54321, 'john@example.com', 9876543210, 'Other notes', 75, 2),
            (3, 'Vaibhav', 'Shah', 'FoodCo', '789 Oak St', 'City', 'Country', 67890, 'jane@example.com', 5678901234, 'Additional notes', 100, 3),
            (4, 'Eesha', 'Reddy', 'Delicious Eats', '987 Pine St', 'City', 'Country', 43210, 'david@example.com', 4321098765, 'Extra notes', 125, 4),
            (5, 'Supradha', 'Phani', 'Tasty Bites', '654 Maple St', 'City', 'Country', 21098, 'sarah@example.com', 8765432109, 'More notes', 150, 5)
        """)

        self.cursor.execute("SELECT status FROM orders LIMIT 5")
        result = self.cursor.fetchone()

        self.assertEqual(result[0], 'sent to admins')

    def test_current_timestamp(self):
        self.cursor.execute("""
            INSERT INTO orders (id, name, lname, company_name, address, city, country, zip_code, email, phone_number, order_notes, price, user_id)
            VALUES 
            (1, 'Lakshmi', 'Gowtham', 'HungerDrop', '123 Main St', 'City', 'Country', 12345, 'john@example.com', 1234567890, 'Some notes', 50, 1),
            (2, 'Kunal', 'Raj', 'Company', '456 Elm St', 'City', 'Country', 54321, 'john@example.com', 9876543210, 'Other notes', 75, 2),
            (3, 'Vaibhav', 'Shah', 'FoodCo', '789 Oak St', 'City', 'Country', 67890, 'jane@example.com', 5678901234, 'Additional notes', 100, 3),
            (4, 'Eesha', 'Reddy', 'Delicious Eats', '987 Pine St', 'City', 'Country', 43210, 'david@example.com', 4321098765, 'Extra notes', 125, 4),
            (5, 'Supradha', 'Phani', 'Tasty Bites', '654 Maple St', 'City', 'Country', 21098, 'sarah@example.com', 8765432109, 'More notes', 150, 5)
        """)

        self.cursor.execute("SELECT created_at FROM orders WHERE id = 1")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result[0])


if __name__ == '__main__':
    unittest.main()
