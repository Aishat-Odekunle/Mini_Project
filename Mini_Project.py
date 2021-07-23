import sys, csv

with open("MINI_PROJECT\products.csv", 'r') as file_1:
    reader = csv.reader(file_1, delimiter =',')
        
with open("MINI_PROJECT\couriers.csv", 'r') as file_2:
    reader_2 = csv.reader(file_2, delimiter = ',')
        
with open("MINI_PROJECT\orders.csv", 'r') as file_3:
    reader_3 = csv.reader(file_3, delimiter = ',')


products_list = [] 

couriers_list = []

orders_list = []
orders_status_list = []


print("Hi, welcome to Aishat's Delight")

def instructions():
    # Displays a set of instructions
    print('Please follow the following instructions.')
    print(f'You have {len(products_list)} item(s) in your basket: {products_list}')
    print(f'You have {len(couriers_list)} courier(s) on your list: {couriers_list}')
    print(f'You have {len(orders_list)} order(s) on your list: {orders_list}')
    
    
def main_menu():
    while True: # If the user inputs a number out of range the app won't break but display appropriate set of instructions.
        user_input = int(input('Input: \n 0 to exit the application \
                                \n 1 to progress to the products menu \
                                \n 2 to progress to the couriers list \
                                \n 3 to progress to the orders list: '))
        #PRODUCTS MENU
        if user_input == 1:
            print(f'You have {len(products_list)} item(s) in your basket: {products_list}')
            user_input_2 = int(input('Input: \n 0 to return to main menu \
                                \n 1 to print the products menu \
                                \n 2 to add a new product and display your basket \
                                \n 3 to update existing items in your basket \
                                \n 4 to remove an item from your basket: '))
            if user_input_2 == 1:
                print(f'You have {len(products_list)} item(s) in your basket: {products_list}') 
            elif user_input_2 == 2:
                new_product_dict = {}
                new_product_dict['name'] = input("Enter a new product name: ").lower()
                new_product_dict['price'] = input("Enter the product price: ").lower()
                print(new_product_dict)
                
                products_list.append(new_product_dict)
                print(f'You now have {len(products_list)} item(s) in your basket: {products_list}')
                
            elif user_input_2 == 3:
                print('index \t item')
                for index, items in enumerate(products_list):
                    print(str(index), '\t', str(items))
                    
                product_index = input(f'You may update an existing item in your basket. \
                                    \n Input a number between 0 to {len(products_list)-1} for the position of the item you wish to update: ')
                item = int(product_index)
                item_new_name = input("input a new item name: ")
                item_new_price = input('Input a new item price: ')
                
                new_product_dict_2 = {}
                new_product_dict_2['name'] = item_new_name
                new_product_dict_2['price'] = item_new_price
                
                #put an if statement to catch when they dont input anything so it remains the same
                
                products_list[item] = new_product_dict_2
                
                print(f'Your item has been updated as follows: {new_product_dict_2}')
                print(f'You now have {len(products_list)} item(s) in your basket: {products_list}')
                

                # for key, value in item.items():
                #     product_update = input(f'Update the item name or price: ')
                #     if product_update == '':
                #         item[key] = value
                #     else:
                #         item[key] = product_update
                
            elif user_input_2 == 4:
                print(f'You have {len(products_list)} item(s) in your basket: {products_list}')
                product_index_2 = int(input(f'Input a number between 0 and {len(products_list)-1} representing the item you wish to remove: '))
                del products_list[product_index_2]
                print(f'You now have {len(products_list)} item(s) in your basket: {products_list}')
                
            elif user_input_2 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Enter a number between 0 and 4')
                
        #COURIERS LIST
        elif user_input == 2: 
            print(f'You have {len(couriers_list)} courier(s) on your list: {couriers_list}')
            user_input_3 = int(input('Input:\n 0 to return to main menu \
                                            \n 1 to print courier list \
                                            \n 2 to add a new courier and display list \
                                            \n 3 to update an existing courier \
                                            \n 4 to remove a courier from your list: '))
            if user_input_3 == 1:
                print(f'You have {len(couriers_list)} courier(s) on your list: {couriers_list}') 
            elif user_input_3 == 2:
                new_courier_dict = {}
                new_courier_dict['name'] = input('Enter a new courier name: ').lower()
                new_courier_dict['phone'] = input("Enter the new courier's phone:  "). lower()
                couriers_list.append(new_courier_dict)
                print(f'You now have {len(couriers_list)} courier(s) on your list: {couriers_list}')
                
            elif user_input_3 == 3:
                print('index \t courier')
                for index, items in enumerate(couriers_list):
                    print(str(index), '\t', str(items))
                    
                courier_index = int(input(f'You may update an existing courier on your list. \
                                            \n Input a number between 0 to {len(couriers_list)-1} for the position of the courier you wish to update: '))
                courier = int(courier_index)
                courier_new_name = input("input a new courier name: ")
                courier_new_phone = input('Input a new courier phone number: ')
                
                new_courier_dict_2 = {}
                new_courier_dict_2['name'] = courier_new_name
                new_courier_dict_2['phone'] = courier_new_phone
                
                #put an if statement to catch when they dont input anything so it remains the same
                
                couriers_list[courier] = new_courier_dict_2
                
                print(f'Your courier has been updated as follows: {new_courier_dict_2}')
                print(f'You now have {len(couriers_list)} courier(s) on your list: {couriers_list}')
                
                # for key, value in courier_item.items():
                #     courier_update = input(f'Update the courier name or phone number: ')
                #     if courier_update == '':
                #         courier_item[key] = value
                #     else:
                #         courier_item[key] = courier_update
                
            elif user_input_3 == 4:
                print(f'You have {len(couriers_list)} courier(s) on your list: {couriers_list}')
                courier_index_2 = int(input(f'Input a number between 0 and {len(couriers_list)-1}. \
                                    \n This represents the index of the courier you wish to remove: '))
                del couriers_list[courier_index_2]
                print(f'You now have {len(couriers_list)} courier(s) on your list: {couriers_list}')
                
            elif user_input_3 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Enter a number between 0 and 4')
                
        #ORDERS LIST
        elif user_input == 3:
            print(f'You have {len(orders_list)} order(s) on your list: {orders_list}')
            user_input_4 = int(input('Input:\n 0 to return to main menu \
                                            \n 1 to print orders list. \
                                            \n 2 to place an order: \
                                            \n add a customer name, address and phone number. \
                                            \n select a courier: \
                                            \n 3 to update existing order status: \
                                            \n 4 to update an existing order:  \
                                            \n 5 to delete an order at index in order list : '))
            if user_input_4 == 1:
                print(f'You have {len(orders_list)} order(s) on your list: {orders_list}')
                
            elif user_input_4 == 2:
                
                new_order_dict = {}
                new_order_dict['customer_name'] = input("Enter the customer's name: ").lower()
                new_order_dict['customer_address'] = input("Enter the customer's address: ").lower()
                new_order_dict['customer_phone'] = input("Enter the customer's phone number: ").lower()
                
                print('index \t product')
                for index, items in enumerate(products_list):
                    print(str(index), '\t', str(items))
                
                products_indexes = (input(f'Enter numbers between 0 and {len(products_list)-1} for the index of the items you want separated by a comma: ').lower().split(','))
                products_indexes_list = [int(i) for i in products_indexes]               
                new_order_dict['items'] = products_indexes_list
                
                print('index \t courier')
                for index, items in enumerate(couriers_list):
                    print(str(index), '\t', str(items))
                new_order_dict['courier'] = int(input(f'Input a number between 0 and {len(couriers_list)-1} to select a courier. '))
                
                new_order_dict['status'] = 'PREPARING'
                
                print(new_order_dict)
                
                orders_list.append(new_order_dict)
                print(orders_list)
                
            elif user_input_4 == 3:
                print('index \t orders_list')
                for index, items in enumerate(orders_list):
                    print(str(index), '\t', str(items))
                    
                order_index = int(input(f'Input a number between 0 to {len(orders_list)-1} for the position of the order status you wish to update: '))
                
                # PRINT order status list with its index values
                #print('index \t orders_status_list')
                #for index, items in enumerate(orders_status_list):
                #    print(str(index), '\t', str(items))
                    
                # GET user input for order status index value
                #order_status_index = int(input(f'Input a number between 0 to {len(orders_status_list) -1} to update your order status: '))
                    
                orders_list[order_index]['status'] = input(f'Update your order status: ')
                
            elif user_input_4 == 4:
                print('index \t orders_list')
                for index, items in enumerate(orders_list):
                    print(str(index), '\t', str(items))
                    
                order_index_2 = int(input(f'To update an existing order -  \
                                    \n Input a number between 0 to {len(orders_list)-1} for the position of the order you wish to update: '))   
                order = int(order_index_2)
                
                order_new_name = input("Input a new order name: ")
                order_new_address = input('Input a new order address: ')
                order_new_phone = input("Input a new order phone number: ")
                
                print('index \t product')
                for index, items in enumerate(products_list):
                    print(str(index), '\t', str(items))
                
                products_indexes_2 = (input(f'Enter numbers between 0 and {len(products_list)-1} for the index of the items you want separated by a comma: ').lower().split(','))
                products_indexes_list_2 = [int(i) for i in products_indexes_2]  
                
                print('index \t courier')
                for index, items in enumerate(couriers_list):
                    print(str(index), '\t', str(items))
                
                order_new_courier = int(input(f'Input a number between 0 and {len(couriers_list)-1} to select a courier. '))

                order_new_status = input('Input a new status for your order: ')
                
                new_order_dict_2 = {}
                new_order_dict_2['customer_name'] = order_new_name
                new_order_dict_2['customer_address'] = order_new_address
                new_order_dict_2['customer_phone'] = order_new_phone
                new_order_dict_2['items'] = products_indexes_list_2
                new_order_dict_2['courier'] = order_new_courier
                new_order_dict_2['status'] = order_new_status
                
                
                #put an if statement to catch when they dont input anything so it remains the same
                
                orders_list[order] = new_order_dict_2
                
                print(f'Your order has been updated as follows: {new_order_dict_2}')
                print(f'You now have {len(orders_list)} orders on your list: {orders_list}')
                
                # order_item = orders_list[int(order_index_2)]
                # for key, value in order_item.items():
                #     order_update = input(f'Update your name, address, phone number, items, courier or status: ')
                #     if order_update == '':
                #         order_item[key] = value
                #     else:
                #         order_item[key] = order_update
                #print(f'Your order has been updated as follows: {order_item}')
                        
            elif user_input_4 == 5:
                print(f'You have {len(orders_list)} order(s) on your list: {orders_list}')
                order_index_3 = int(input(f'Input a number between 0 and {len(orders_list)-1}. \
                                    \n This represents the index of the order you wish to remove: '))
                del orders_list[order_index_3]
                print(f'You now have {len(orders_list)} order(s) on your list: {orders_list}')
                
            elif user_input_4 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Enter a number between 0 and 5')
                
        elif user_input == 0: #After every operation, users can input 0 to exit.
            #SAVE products_list to products.csv, couriers_list to couriers.csv and orders_list to orders.csv
            
            keys = products_list[0].keys()
            with open("MINI_PROJECT\products.csv", "a") as file_1:
                dict_writer_1 = csv.DictWriter(file_1, keys)
                dict_writer_1.writeheader()
                dict_writer_1.writerows(products_list)
            
            keys = couriers_list[0].keys()
            with open("MINI_PROJECT\couriers.csv", "a") as file_2:
                dict_writer_2 = csv.DictWriter(file_2, keys)
                dict_writer_2.writeheader()
                dict_writer_2.writerows(couriers_list)
                
            keys = orders_list[0].keys()
            with open("MINI_PROJECT\orders.csv", "a") as file_3:
                dict_writer_3 = csv.DictWriter(file_3, keys)
                dict_writer_3.writeheader()
                dict_writer_3.writerows(orders_list)
            
            sys.exit(0)
            
instructions()
main_menu()