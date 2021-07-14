import sys
#LOAD products list from products.txt
#LOAD couriers list from couriers.txt
file_1 = open('MINI_PROJECT\products.txt', 'r')
lines_1 = file_1.readlines()
file_1.close()

file_2 = open('MINI_PROJECT\couriers.txt', 'r')
lines_2 = file_2.readlines()
file_2.close()


print("Hi, welcome to Aishat's Delight")

product_names = input("Please enter the products you want: ").lower().split(',')
#The strip() method removes any leading and trailing characters (space is the default leading character to remove).
products = [word.strip() for word in product_names]

courier_names = input("Please enter the couriers you want: ").lower().split(',')
couriers = [word.strip() for word in courier_names]

def instructions():
    #This displays a set of instructions
    print('Please follow the following instructions.')
    print(f'You have {len(products)} items in your basket: {products}')
    print(f'You have {len(couriers)} couriers on your list: {couriers}')
    
    
def main_menu():
    while True: # Even if user inputs a number out of range the app won't break but display appropriate set of instructions.
        user_input = int(input('Input: \n 0 to exit the application \
                                \n 1 to progress to the products menu \
                                \n 2 to progress to the couriers list '))
        if user_input == 1:
            print(f'You have {len(products)} items in your basket: {products}')
            user_input_2 = int(input('Input: \n 0 to return to main menu \
                                \n 1 to print the products menu \
                                \n 2 to add a new product and display your basket \
                                \n 3 to print the index and items in your basket with further options \
                                \n 4 to remove an item from your basket '))
            if user_input_2 == 1:
                print(f'You have {len(products)} items in your basket: {products}') 
            elif user_input_2 == 2:
                user_input_3 = input('Enter a new item to add to your basket: ').lower()
                products.append(user_input_3)
                print('Your basket now has the following items: ', products)
            elif user_input_2 == 3:
                print('index \t item')
                for index, items in enumerate(products):
                    print(str(index), '\t', str(items))
                    
                user_input_index = int(input(f'You may add a new item to your basket. \
                                    \n Input a number between 0 to {len(products)} for the position of the item you wish to add: '))
                user_input_item = input('Enter a new item you wish to add: ')
                    
                #The list insert() method inserts an element to the list at the specified index
                products.insert(user_input_index, user_input_item)
                print(f'You now have the following items in your basket: {products}')
                    
            elif user_input_2 == 4:
                print(f'You have the following items in your basket: {products}')
                new_user_input_index = int(input(f'Input a number between 0 and {len(products)-1} representing the product you wish to remove: '))
                del products[new_user_input_index]
                print(f'Your basket now has the following items: {products}')
                
            elif user_input_2 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Enter a number between 0 and 4')
                
        elif user_input == 2: 
            print(f'You have {len(couriers)} couriers on your list: {couriers}')
            user_input_4 = int(input('Input:\n 0 to return to main menu \
                                            \n 1 to print courier list \
                                            \n 2 to add a new courier and display list \
                                            \n 3 to print the index and couriers on your list with further options \
                                            \n 4 to remove a courier from your list: '))
            if user_input_4 == 1:
                print(f'You have {len(couriers)} couriers on your list: {couriers}') 
            elif user_input_4 == 2:
                user_input_5 = input('Enter a new courier to add to your list: ').lower()
                couriers.append(user_input_5)
                print('Your list now has the following couriers: ', couriers)
            elif user_input_4 == 3:
                print('index \t courier')
                for index, items in enumerate(couriers):
                    print(str(index), '\t', str(items))
                    
                user_input_courier_index = int(input(f'You may add a new courier to your list. \
                                            \n Input a number between 0 to {len(couriers)} for the position of the courier you wish to add: '))
                user_input_courier = input('Enter a new courier you wish to add: ')
                    
                #The list insert() method inserts an element to the list at the specified index
                couriers.insert(user_input_courier_index, user_input_courier)
                print(f'You now have the following couriers on your list: {couriers}')
                    
            elif user_input_4 == 4:
                print(f'You have the following couriers on your list: {couriers}')
                new_user_input_courier_index = int(input(f'Input a number between 0 and {len(couriers)-1}. \
                                                \n This represents the index of the courier you wish to remove: '))
                del couriers[new_user_input_courier_index]
                print(f'Your basket now has the following couriers: {couriers}')
                
            elif user_input_4 == 0: # If the user input 0 above, return to main menu
                x = instructions()
            else:
                print('Enter a number between 0 and 4')
        elif user_input == 0: #After every operation, users can input 0 to exit.
            #SAVE product list to products.txt
            #SAVE courier list to couriers.txt
            with open("MINI_PROJECT\products.txt", "a") as p:
                products_str = ' '. join([str(item) for item in products])
                p.write(products_str + '\n')
            
            
            with open("MINI_PROJECT\couriers.txt", "a") as c:
                couriers_str = ' '. join([str(item) for item in couriers])
                c.write(couriers_str + '\n')
        
            sys.exit(0)
            
instructions()
main_menu()



'''
elif user_input == 1:
    print(products)
    
user_input2 = int(input("Enter a product menu option please:"))

if user_input2 == 0:
    return 
elif user_input2 == 1:
    print(products)
elif user_input2 == 2:
    new_product = input("Enter a new product name")
    products.append(new_product)
elif user_input2 == 3:
    print("Products index value are: ")
    for index in range(len(products)):
        print(index, product)
        print(products[index])
        product_index_value = input("Enter a product index value:")
        new_product2 = input("Enter another new product name: ")
        products.append(new_product2)
elif user_input2 == 4:
    print(products)
    product_index_value2 = input("Enter another product index value:")
    del products[product_index_value2]


ELSE IF user input is 4:
# STRETCH GOAL - DELETE product
PRINT products list
GET user input for product index value
DELETE product at index in products 
'''