import sqlite3

class DataBase:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = 'DataBase.db'
    
    def open(self):
        self.conn = sqlite3.connect( self.db_name )
        self.cursor = self.conn.cursor()
        
    def close(self):
        self.cursor.close()
        self.conn.close()
        
    def get_all_items(self):
        self.open()
        
        self.cursor.execute("SELECT * FROM items")
        data = self.cursor.fetchall()
        
        self.close()
        return data
    
    def get_item(self, id):
        self.open()
        
        self.cursor.execute("SELECT * FROM items WHERE id==(?)", [id])
        data = self.cursor.fetchone()
        
        self.close()
        return data

    def get_categories(self):
        self.open()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
    

    def get_category_items(self, id):
        self.open()
        self.cursor.execute("SELECT * FROM items WHERE category_id==(?)", [id])
        data = self.cursor.fetchall()
        self.close()
        return data

    def add_order(self, *data):
        self.open()
        self.cursor.execute('''INSERT INTO orders (item_id, name, phone, city, address, amount, cost)
                            VALUES((?), (?), (?), (?), (?), (?), (?))''', [*data])
        self.conn.commit()
        self.close()

        