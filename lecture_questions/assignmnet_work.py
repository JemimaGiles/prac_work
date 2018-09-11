PRODUCT_FILE = 'file.csv'
MENU_STRING = '...'


def main():
    products = load_products()
    # create function for this

    print(MENU_STRING)
    choice = input()
    while choice != 'q':
        if choice == 'l':
            print("list")
        #     change this to a def list products
        #   list_products(products)
        elif choice == 's':
            print("swap")
        else:
            print("invalid")

        print(MENU_STRING)
        choice = input()
    print("fin")


def load_prodcuts():
    products = []
    return products


def list_products():


def swap_item(products):
    list_products(products)
    number = int(input("what num"))
    print(products[number])
#      we need to do exception based error checking
# copy exisitn patter from online


main()
