from model.model import Model
from view.view import View
from model import  mvc_exceptions as m_e

class Controller:


    def __init__(self):
        #instancia de model
        self.model = Model()
        #instancia de view
        self.view = View()

    def create_a_product(self, id_product, name, brand, category, price, weight, batch):
        try:
            self.model.create_a_product(
                id_product, name, brand, category, price, weight, batch
            )
        except m_e.item_already_stored as e:
            self.view.item_already_stored_error(e)

    def show_all_products(self):
        #lista de productos
        products_in_db = self.model.read_all_products()
        #llama a la vista para desplegar los productos
        self.view.show_all_products(products_in_db, 1)

    def show_a_product(self, name):
        #shows details for a specific product
        try:
            product = self.model.read_a_product(name)
            self.view.show_a_product(product)
        except m_e.item_not_stored as e:
            self.view.item_not_stored_error(e)

    def insert_products(self):
        #insert data in the model for products
        self.create_a_product(1, 'iPhone 8', 'Apple', 'Phones', 1000, 0.1, 'L200')
        self.create_a_product(2, 'Galaxy S9', 'Samsung', 'Phones', 900, 0.2, 'X500')
        self.create_a_product(3, 'Monitor 15"', 'BenQ', 'Monitors', 200, 1.5, 'k400')

    def create_a_client(self, id_client, name, email, address):
        try:
            self.model.create_a_product(
                id_client, name, name, email, address
            )
        except m_e.item_already_stored as e:
            self.view.item_already_stored_error(e)

   # def insert_clients(self):
   #     #insert data in the model for clients
   #     self.create_a_client()


    def start(self):
        self.view.start_view()
        self.view.menu()
        op = input()
        if op == '1':
            print('opcion 1')
            self.view.insert_a_product()
            a = input()
            b = input()
            c = input()
            d = input()
            e = input()
            f = input()
            self.create_a_product(4,a,b,c,d,e,f)
        else:
            if op == '2':
