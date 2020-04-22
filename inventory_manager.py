# Product lists
product_names = ['soft drink', 'onion rings', 'small fries']
product_costs = [0.99, 1.29, 1.49]
product_quantity = [10, 5, 20]

def search(product):
    if product in product_names:
        ind = product_names.index(product)                                              # Get index of product to use to get the price
        print('We sell \"{}\" at {} per unit'.format(product, product_costs[ind]))
        print('We currently have {} in stock'.format(product_quantity[ind]))
    else:
        print('Sorry, we don\'t sell \"{}\"'.format(product))
    print()

def list_products():
    # Headings
    title_product = 'Product'
    title_price = 'Price'
    title_quan = 'Quantity'

    # Print with predefined spacing each product and attributes
    print('%-20s %-8s %s' %(title_product, title_price, title_quan))
    for x in range(len(product_names)):
        print('%-20s %-8s %s' %(product_names[x], product_costs[x], product_quantity[x]))
    print()

def add_product():
    # Get name checking input
    name = str(input('Enter a new product name: '))
    while name in product_names:
        print('Sorry, we already sell that product. Try again.')
        name = str(input('Enter a new product name: '))
    
    # Get price checking input
    price = float(input('Enter a product cost: '))
    while price <= 0:
        print('Invalid cost. Try again.')
        price = float(input('Enter a product cost: '))

    # Get quantity checking input
    quant = int(input('How many of these products do we have? '))
    while quant <= 0:
        print('Invalid quantity. Try again.')
        quant = int(input('How many of these products do we have? '))

    # After verifying all variables put them into their respective lists
    product_names.append(name)
    product_costs.append(price)
    product_quantity.append(quant)
    print('Product added!\n')

def remove_product():
    name = str(input('Enter product name: '))
    if name not in product_names:
        print('Product does not exist. Can\'t remove.\n')
    else:
        # Get index of name then delete that index in each list
        ind = product_names.index(name)
        del product_names[ind]
        del product_quantity[ind]
        del product_costs[ind]
    print()

def update_product():
    name = str(input('Enter product name: '))
    if name not in product_names:                                           # Check for name in product_names
        print('Product does not exist. Can\'t update.\n')
    else:
        ind = product_names.index(name)                                     # Get index of product
        print('What would you like to update?')
        choice = input('(n)ame, (c)ost or (q)uantity: ')
        if choice == 'n':
            name = str(input('Enter a new name: '))
            while name in product_names:
                print('Duplicate name!')
                name = str(input('Enter a new name: '))
            product_names[ind] = name
        
        elif choice == 'c':
            price = float(input('Enter new cost: '))
            while price <= 0:
                print('Invalid cost. Try again.')
                price = float(input('Enter new cost: '))
            product_costs[ind] = price
        
        elif choice == 'q':
            quant = int(input('Enter a new quantity: '))
            while quant <= 0:
                print('Invalid quantity. Try again.')
                quant = int(input('Enter a new quantity: '))
            product_quantity[ind] = quant
        
        else:
            print('Invalid option')
            return
    print()

def generate_report():
    # Get most expensive product
    most_exp = 0
    most_exp_ind = int(0)
    for x in range(len(product_costs)):
        if product_costs[x] > most_exp:
            most_exp = product_costs[x]
            most_exp_ind = x

    # Get least expensive product
    least_exp = most_exp
    least_exp_ind = int(0)
    for y in range(len(product_costs)):
        if product_costs[y] < least_exp:
            least_exp = product_costs[y]
            least_exp_ind = y

    # Get total value of all products
    total_value = 0
    for z in range(len(product_names)):
        total_value += product_quantity[z] * product_costs[z]

    print('Most expensive product:      {} ({})'.format(most_exp, product_names[most_exp_ind]))
    print('Least expensive product:     {} ({})'.format(least_exp, product_names[least_exp_ind]))
    print('Total value of all products: {}\n'.format(round(total_value, 2)))

def main():
    choice = ''
    while choice != 'q':
        choice = input('(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ')
        if choice == 'q':
            print('See you soon!')
            break
        elif choice == 's':
            search(input('Enter a product name: '))
        elif choice == 'l':
            list_products()
        elif choice == 'a':
            add_product()
        elif choice == 'r':
            remove_product()
        elif choice == 'u':
            update_product()
        elif choice == 'e':
            generate_report()
        else:
            print('Invalid input. Try again.')

main()