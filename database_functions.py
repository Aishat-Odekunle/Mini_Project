import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


def fetch_products():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    # # A cursor is an object that represents a DB cursor,
    # # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    # # Execute SQL query
    cursor.execute('SELECT * FROM products')
    
    products_list = []
    rows = cursor.fetchall()
    for row in rows:
        products_list.append({'product_id': row[0], 'product_name': row[1], 'product_price': row[2]})
        
    cursor.close()
    connection.close()
    return products_list


def fetch_couriers():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM couriers')
    
    rows = cursor.fetchall()
    
    couriers_list = []
    for row in rows:
        couriers_list.append({'courier_id': row[0], 'courier_name': row[1], 'phone_number': row[2]})
    
    cursor.close()
    connection.close()
    return couriers_list

    
def fetch_orders():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM orders')
    
    rows = cursor.fetchall()
    
    orders_list = []
    for row in rows:
        orders_list.append({'order_id': row[0], 'customer_name': row[1], 'address': row[2],
        'phone_number': row[3], 'courier': row[4], 'items': row[5], 'order_status': row[6]})
    
    cursor.close()
    connection.close()
    return orders_list
    

def products_available():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products')
    
    rows = cursor.fetchall()
    for row in rows:
        print("product_id: ", row[0], "product_name: ", row[1], "product_price: ", row[2]) 

    cursor.close()
    connection.close()
    
    
def couriers_available():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM couriers')
    
    rows = cursor.fetchall()
    for row in rows:
        print("courier_id: ", row[0], "courier_name: ", row[1], "phone_number: ", row[2])

    cursor.close()
    connection.close()
    
    
def orders_available():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM orders')
    
    rows = cursor.fetchall()
    for row in rows:
        print("order_id: ", row[0], "customer_name: ", row[1], "address: ", row[2], "phone_number: ", 
                row[3], "courier: ", row[4], "items: ", row[5], "status: ", row[6])
    
    cursor.close()
    connection.close()   
    
    
def orders_statuses():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM orders_statuses')
    
    rows = cursor.fetchall()
    for row in rows:
        print("order_status_id: ", row[0], "order_status: ", row[1])
    
    cursor.close()
    connection.close()
    
    
def insert_into_products(name, price):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (name , price)
    command =  "INSERT INTO products (product_name, product_price) VALUES ( %s, %s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()


def insert_into_couriers(name, phone):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (name, phone)
    command =  "INSERT INTO couriers (courier_name, phone_number) VALUES (%s, %s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()
    
    
def insert_into_orders(name, address, phone, courier_id, items, order_status):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )

    cursor = connection.cursor()
    values = (name, address, phone, courier_id, items, order_status)
    command =  "INSERT INTO orders (customer_name, customer_address, phone_number, courier, items, order_status) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(command, values)

    connection.commit()
    cursor.close()
    connection.close()
    
    
def update_product(name, price, id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (name, price, id)
    command =  "UPDATE products SET product_name = (%s), product_price = (%s) WHERE product_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()


def update_courier(name, phone, id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (name, phone, id)
    command =  "UPDATE couriers SET courier_name = (%s), phone_number = (%s) WHERE courier_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()
    
    
def update_order(customer_name, customer_address, customer_phone, courier, items, order_id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (customer_name, customer_address, customer_phone, courier, items, order_id)
    command =  "UPDATE orders SET customer_name = (%s), customer_address = (%s), phone_number = (%s), \
                \n courier = (%s), items = (%s) WHERE order_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()
    
    
def update_order_status(order_status_id, order_id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (order_status_id, order_id)
    command =  "UPDATE orders SET order_status = (%s) WHERE order_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()
    
    
def delete_product(id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (id)
    command =  "DELETE FROM products WHERE product_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()


def delete_courier(id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (id)
    command =  "DELETE FROM couriers WHERE courier_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()
    
    
def delete_order(id):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
)
    
    cursor = connection.cursor()
    values = (id)
    command =  "DELETE FROM orders WHERE order_id = (%s)"
    cursor.execute(command, values)
    
    connection.commit()
    cursor.close()
    connection.close()



