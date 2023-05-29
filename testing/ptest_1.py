import mysql.connector

sql_query = """
    CREATE TABLE `admins` (
        `id` int(3) NOT NULL,
        `adminname` varchar(200) NOT NULL,
        `email` varchar(200) NOT NULL,
        `mypassword` varchar(200) NOT NULL,
        `created_at` timestamp NOT NULL DEFAULT current_timestamp()
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='6390',
    database='admin'
)

try:
    cursor = conn.cursor()
    cursor.execute(sql_query)
    conn.commit()
    print("Integration test passed: 'admins' table created successfully.")

except mysql.connector.Error as e:
    conn.rollback()

    print("Integration test failed:", str(e))

finally:
    conn.close()