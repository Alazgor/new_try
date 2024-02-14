import datetime
import logging

logging.basicConfig(level=logging.DEBUG, filename='cafe.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self, menu_type, items):
        self.menu_type = menu_type
        self.items = items

    def display_menu(self):
        print(f'Menu: {self.menu_type}')
        for item in self.items:
            print(f'{item.name} - ${item.price:.2f}')


class Table:
    def __init__(self, table_type):
        self.table_type = table_type
        self.is_occupied = False
        self.surname = None
        self.reservation_time = None

    def occupy(self, surname):
        self.is_occupied = True
        self.surname = surname
        self.reservation_time = datetime.datetime.now()

    def vacate(self):
        self.is_occupied = False
        self.surname = None
        self.reservation_time = None


class Cafeteria:
    def __init__(self, number_single_tables, number_double_tables, number_family_tables):
        self.tables = []
        self.orders = {}
        self.menus = {
            'Breakfast': [MenuItem('Pancakes', 8.99), MenuItem('Salad', 6.99)],
            'Drinks': [MenuItem('Still water', 1.99), MenuItem('Red wine', 5.50)]
        }

        self.create_tables(number_single_tables, 'single')
        self.create_tables(number_double_tables, 'double')
        self.create_tables(number_family_tables, 'family')

    def create_tables(self, number, table_type):
        for _ in range(number):
            table = Table(table_type)
            self.tables.append(table)

    def display_menu(self, menu_type):
        menu = self.menus.get(menu_type)
        if menu:
            Menu(menu_type, menu).display_menu()
        else:
            print("Menu not found.")

    def display_table_status(self):
        for i, table in enumerate(self.tables):
            status = 'Occupied' if table.is_occupied else 'Free'
            print(f'Table {i + 1} ({table.table_type}): {status}')

    def make_reservation(self, surname, table_type):
        for table in self.tables:
            if table.table_type == table_type and not table.is_occupied:
                table.occupy(surname)
                print(f'Reservation for {table.table_type} table is accepted')
                return
        print('Sorry, we don\'t have free tables')

    def check_reservation(self, surname):
        for table in self.tables:
            if table.surname == surname:
                print(f'Table {self.tables.index(table) + 1} ({table.table_type}) is reserved for {surname}')
                return
        print('No reservation found for this surname.')

    def make_order(self, table_index, item_name, quantity):
        if table_index < 0 or table_index >= len(self.tables):
            print('Invalid table number.')
            return

        table = self.tables[table_index]
        if not table.is_occupied:
            print('Table is not occupied.')
            return

        if table_index not in self.orders:
            self.orders[table_index] = []

        for _ in range(quantity):
            self.orders[table_index].append(item_name)

    def display_menu_names(self):
        print('Menus for today:')
        for menu_type in self.menus:
            print(menu_type)

    def display_bill(self, table_index, tips=0):
        if table_index < 0 or table_index >= len(self.tables):
            print('Invalid table number.')
            return

        if table_index not in self.orders:
            print('No orders found for this table.')
            return

        total_price = 0
        for item_name in self.orders[table_index]:
            for menu in self.menus.values():
                for menu_item in menu:
                    if menu_item.name == item_name:
                        total_price += menu_item.price
                        break

        total_price += total_price * tips / 100
        print(f'Total bill for table {table_index + 1}: ${total_price:.2f}')
        logging.info(f'Bill for table {table_index + 1}: ${total_price:.2f}')


def main():
    cafe = Cafeteria(3, 5, 4)
    customer_surname = input('What is your surname: ')
    cafe.check_reservation(customer_surname)  # Check if the customer has a reservation

    if input('Do you want to make a reservation? (yes/no): ').lower() == 'yes':
        table_type = input('What kind of table do you prefer: single, double, or family? ')
        cafe.make_reservation(customer_surname, table_type)

    cafe.check_reservation(customer_surname)  # Check reservation status again

    while True:
        cafe.display_menu_names()
        customer_menu = input('Choose a menu: ')
        if not customer_menu:
            break

        cafe.display_menu(customer_menu)
        item_to_order = input('Choose an option: ')
        item_quantity = int(input(f'How many {item_to_order} do you want? '))

        table_index = int(input('Enter table number: ')) - 1
        cafe.make_order(table_index, item_to_order, item_quantity)

    tips = int(input('Enter % of tips: '))
    table_index = int(input('Enter table number for bill: ')) - 1
    cafe.display_bill(table_index, tips)


if __name__ == "__main__":
    main()
