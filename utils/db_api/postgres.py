import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST,
                                           port=DB_PORT)
        self.cursor = self.connection.cursor()

    async def get_categories(self):
        try:
            self.cursor.execute(
                "SELECT * FROM products_category"
            )
            result = self.cursor.fetchall()
            return result if result else []
        except Exception as e:
            print(f"Database Error: {e}")

    async def get_sub_categories(self, category_id):
        try:
            self.cursor.execute(
                f"SELECT * FROM products_subcategory WHERE category_id_id={category_id}"
            )
            result = self.cursor.fetchall()
            return result if result else []
        except Exception as e:
            print(f"Database Error: {e}")

    async def get_product(self, subcategory_id):
        try:
            self.cursor.execute(
                f"SELECT * FROM products_product WHERE sub_id_id={subcategory_id}"
            )
            result = self.cursor.fetchall()
            return result if result else []
        except Exception as e:
            print(f"Database Error: {e}")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    async def get_products(self, product_id):
        try:
            self.cursor.execute(
                f"SELECT * FROM products_product WHERE id={product_id}"
            )
            result = self.cursor.fetchall()
            return result if result else []
        except Exception as e:
            print(f"Database Error: {e}")

    async def get_products_sub(self, sub_id_id):
        try:
            self.cursor.execute(
                f"SELECT * FROM products_subcategory WHERE id={sub_id_id}"
            )
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Database Error: {e}")
