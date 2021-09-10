import sys, csv
import database_functions as db

# print('\n')
fp = db.fetch_products()
# print(fp)

fc = db.fetch_couriers()
# print(fc)

fo = db.fetch_orders()
# print(fo)


def instructions():
    print("\n Hi, welcome to Aishat's Delight \n") 
    print(' Please follow the instructions stated below.')

def main_menu():
    while True: # If the user inputs a number out of range,
        # the app won't break but display appropriate set of instructions.
        user_input = int(input('\n Input: \
                                \n 0 to exit the application \
                                \n 1 to progress to the products menu \
                                \n 2 to progress to the couriers list \
                                \n 3 to progress to the orders list: '))
        print('\n')
        #PRODUCTS
        if user_input == 1:
            user_input_2 = int(input('Input: \n 0 to return to main menu \
                                \n 1 to print the products menu \
                                \n 2 to add a new product \
                                \n 3 to update a product \
                                \n 4 to delete a product: '))
            print('\n')
            if user_input_2 == 1:
                # GET all products from products table
                db.products_available()
                
            elif user_input_2 == 2:
                new_product_dict = {}
                new_product_dict['name'] = input("Enter a new product name: ").lower()
                new_product_dict['price'] = input("Enter the product price: ").lower()
                
                # INSERT product into products table
                db.insert_into_products(new_product_dict['name'], new_product_dict['price'])
                
            elif user_input_2 == 3:
                # GET all products from products table
                db.products_available()
                print('\n')
                product_id = input("Enter a product_id from the above: ")
                product_new_name = input("input a new name for the product: ")
                product_new_price = input('Input a new price for the product: ')
                
                # IF any inputs are empty, do not update them
                # UPDATE properties for product in product table
                
                # if product_id or product_new_name or product_new_price == '':
                    # product_id = 
                
                db.update_product(product_new_name, product_new_price, product_id)
                
            elif user_input_2 == 4:
                # GET all products from products table
                db.products_available()
                print('\n')
                product_id_2 = input("Enter a product_id from the above: ")
                db.delete_product(product_id_2)
                
            elif user_input_2 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Please enter a number between 0 and 4')
                
                
        #COURIERS
        elif user_input == 2: 
            user_input_3 = int(input('Input:\n 0 to return to main menu \
                                            \n 1 to print the couriers list \
                                            \n 2 to add a new courier \
                                            \n 3 to update an existing courier \
                                            \n 4 to delete a courier: '))
            print('\n')
            if user_input_3 == 1:
                # couriers_available()
                db.couriers_available()
                
            elif user_input_3 == 2:
                
                new_courier_dict = {}
                new_courier_dict['name'] = input("Enter a new courier name: ").lower()
                new_courier_dict['phone'] = input("Enter the courier's phone number: ").lower()
                
                # INSERT courier into courier table
                db.insert_into_couriers(new_courier_dict['name'], new_courier_dict['phone'])
                
            elif user_input_3 == 3:
                # GET all couriers from couriers table
                db.couriers_available()
                print('\n')
                
                courier_id = input("Select a courier_id from the above: ")
                courier_new_name = input("input a new courier name: ")
                courier_new_phone = input("Input the new courier's phone number: ")
                
                # IF an input is empty, do not update its respective table property
                # if product_id or product_new_name or product_new_price == '':
                
                # UPDATE properties for courier in courier table
                db.update_courier(courier_new_name, courier_new_phone, courier_id)
                
                
            elif user_input_3 == 4:
                # GET all couriers from couriers table
                db.couriers_available()
                print('\n')
                
                courier_id_2 = input("Select a courier_id from the above: ")
                db.delete_courier(courier_id_2)
                
            elif user_input_3 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Please enter a number between 0 and 4')
                
        #ORDERS
        elif user_input == 3:
            # print(f'You have {len(orders_list)} order(s) on your list: {orders_list}')
            user_input_4 = int(input('Input:\n 0 to return to main menu \
                                            \n 1 to print orders list. \
                                            \n 2 to place an order: add a customer name, address, phone number and select a courier \
                                            \n 3 to update existing order status: \
                                            \n 4 to update an existing order:  \
                                            \n 5 to delete an order: '))
            print('\n')
            if user_input_4 == 1:
                db.orders_available()
                
            elif user_input_4 == 2:
                
                new_order_dict = {}
                new_order_dict['customer_name'] = input("Enter the customer's name: ").lower()
                new_order_dict['customer_address'] = input("Enter the customer's address: ").lower()
                new_order_dict['customer_phone'] = input("Enter the customer's phone number: ").lower()
                print('\n')
                
                # products_available()
                db.products_available()
                print('\n')
                
                products_indexes = (input(f'Enter the product_id(s) for the products you want separated by a comma: ').lower().split(','))
                products_indexes_list = [int(i) for i in products_indexes]               
                new_order_dict['items'] = str(products_indexes_list)
                
                print('\n')
                #couriers_available()
                db.couriers_available()
                print('\n')
                new_order_dict['courier_id'] = int(input(f'Input a courier_id to select a courier. '))
                print('\n')
                new_order_dict['order_status'] = 1
                
                #Insert order into orders table here
                db.insert_into_orders(new_order_dict['customer_name'], new_order_dict['customer_address'], 
                                    new_order_dict['customer_phone'], new_order_dict['courier_id'],  
                                    new_order_dict['items'], new_order_dict['order_status'])
                
                print("You have successfully placed your order. Your order is currently being prepared.")
                
            elif user_input_4 == 3:
                # GET all orders from orders table
                db.orders_available()
                print('\n')
                # GET user input for order ID
                order_id = int(input("Enter an order_id from the above: "))
                print('\n')
                
                # GET all order statuses from order_status table
                db.orders_statuses()
                print('\n')
                # GET user input for order status ID
                order_status_id = int(input("Enter an order_status_id from the above: "))
                
                # UPDATE status for order
                db.update_order_status(order_status_id, order_id)
                
            elif user_input_4 == 4:
                # GET all orders from orders table
                db.orders_available()
                print('\n')
                order_id_2 = input("Enter an order_id from the above: ")
                print('\n')
                
                # GET user input for customer name
                # GET user input for customer address
                # GET user input for customer phone number
                customer_new_name = input("Input a new customer name: ")
                customer_new_address = input('Input a new customer address: ')
                customer_new_phone = input("Input a new customer phone number: ")
                print('\n')
                
                # GET all products from products table
                db.products_available()
                print('\n')
                products_indexes_2 = (input('Enter the product_id(s) for the items you want separated by a comma: ').lower().split(','))
                
                products_indexes_list_2 = [int(i) for i in products_indexes_2]  
                
                string_indexes = str(products_indexes_list_2)
                print('\n')
                
                # GET all couriers from couriers table
                db.couriers_available()
                print('\n')
                order_new_courier = int(input('Input a courier_id to select a new courier. '))
                
                # UPDATE order in orders table
                db.update_order(customer_new_name, customer_new_address, customer_new_phone, order_new_courier,
                            string_indexes, order_id_2)
                
            elif user_input_4 == 5:
                
                # STRETCH GOAL - DELETE order
                db.orders_available()
                print('\n')
                order_id_3 = input("Enter an order_id from the above to delete the order: ")
                
                db.delete_order(order_id_3)
                
            elif user_input_4 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Please enter a number between 0 and 5')
                
        elif user_input == 0: #After every operation, users can input 0 to exit.
            #SAVE products_list to products.csv, couriers_list to couriers.csv and orders_list to orders.csv
            # print(fp)
            # print('\n')
            fieldnames_1 = ['product_id', 'product_name', 'product_price']
            with open("products.csv", "w", newline='') as file_1:
                dict_writer_1 = csv.DictWriter(file_1, fieldnames=fieldnames_1)
                dict_writer_1.writeheader()
                dict_writer_1.writerows(fp)
                
                
            # print(fc)
            # print('\n')
            fieldnames_2 = ['courier_id', 'courier_name', 'phone_number']
            with open("couriers.csv", "w", newline='') as file_2:
                dict_writer_2 = csv.DictWriter(file_2, fieldnames=fieldnames_2)
                dict_writer_2.writeheader()
                dict_writer_2.writerows(fc)
                
                
            # print(fo)
            # print('\n')
            fieldnames_3 = ['order_id', 'customer_name', 'address', 
                            'phone_number', 'courier', 'items', 'order_status']
            with open("orders.csv", "w", newline='') as file_3:
                dict_writer_3 = csv.DictWriter(file_3, fieldnames=fieldnames_3)
                dict_writer_3.writeheader()
                dict_writer_3.writerows(fo)
            
            
            sys.exit(0)
            
instructions()
main_menu()