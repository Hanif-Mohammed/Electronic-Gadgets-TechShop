import pymysql
def connect_db():
    try:
        return pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='techshop'
        )
    except pymysql.MySQLError as e:
        print(f"Database connection failed: {e}")
        return None
connection = connect_db()
if connection:
    print("Connected to the database successfully!")
    connection.close()
