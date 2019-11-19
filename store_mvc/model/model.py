from model.client import Client
from .product import Product
from . import mvc_exceptions as m_e


class Model:

    def __init__(self):
        self.products = []
        self.clients = []

    # metodos de producto

    def search_product(self, name):
        for idx, product in enumerate(self.products):
            if product.name.lower() == name.lower():
                return idx
        return -1

    def search_product_by_category(self, category):
        products_category = []
        for idx, product in enumerate(self.products):
            if product.category.lower() == category.lower():
                products_category.append(product)

        return products_category

    def search_product_by_price_range(self, inf_lim, sup_lim):
        products_by_price = []
        for idx, product in enumerate(self.products):
            if (product.price >= inf_lim) and (product.price <= sup_lim):
                products_by_price.append(product)

        return products_by_price

    def create_a_product(self, id_product, name='', brand='', category='', price=0, weight=0, batch=''):
        idx = self.search_product(name)
        if idx < 0:
            self.products.append(
                Product(id_product, name, brand, category, price, weight, batch)
            )
        else:
            raise m_e.item_already_stored('Product "{}" already stored'.format(name.upper()))

    def read_all_products(self):
        return self.products

    def read_a_product(self, name):
        idx = self.search_product(name)
        if idx > -1:
            return self.products[idx]
        else:
            raise m_e.item_not_stored('Can\'t read "{}" because it\'s not stored'.format(name.upper()))

    def update_a_product(self, old_name, new_name, new_brand, new_category, new_price, new_weight, new_batch):
        idx = self.search_product(old_name)
        if idx > -1:
            if self.products[idx].name.lower() != new_name.lower():
                if new_name == '':
                    new_name = self.products[idx].name
                if new_brand == '':
                    new_brand = self.products[idx].brand
                if new_category == '':
                    new_category = self.products[idx].category
                if new_price == '':
                    new_price = self.products[idx].price
                if new_weight == '':
                    new_weight = self.products[idx].weight
                if new_batch == '':
                    new_batch = self.products[idx].batch
                new_product = Product(
                    self.products[idx].id_product, new_name, new_brand, new_category, new_price, new_weight, new_batch
                )
                old_product = self.products[idx]
                self.products[idx] = new_product

            else:
                raise m_e.item_already_stored(
                    'Can\'t update "{}" because it\'s already stored'.format(new_name.upper())
                )
        else:
            raise m_e.item_not_stored('Cant\'t update "{}" because it\'s not stored'.format(old_name.upper()))
        return old_product, new_product

    def delete_a_product(self, name):
        idx = self.search_product(name)
        if idx > -1:
            del self.products[idx]
        else:
            raise m_e.item_not_stored('Can\'t delete "{}" because it\'s not stored'.format(name.upper()))

    # metodos de cliente

    def search_client(self, name):
        for idx, client in enumerate(self.clients):
            if client.name.lower() == name.lower():
                return idx
        return -1

    def create_a_client(self, id_client, name='', email='', address='', phone='', rfc=''):
        idx = self.search_client(name)
        if idx < 0:
            self.clients.append(
                Product(id_client, name, email, address, phone, rfc)
            )
        else:
            raise m_e.item_already_stored('Client "{}" already stored'.format(name.upper()))

    def read_all_clients(self):
        return self.clients

    def read_a_client(self, name):
        idx = self.search_client(name)
        if idx > -1:
            return self.clients[idx]
        else:
            raise m_e.item_not_stored('Can\'t read "{}" because it\'s not stored'.format(name.upper()))

    def update_a_client(self, old_name, new_name, new_email, new_address, new_phone, new_rfc):
        idx = self.search_client(old_name)
        if idx > -1:
            if self.clients[idx].name.lower() != new_name.lower():
                if new_name == '':
                    new_name = self.clients[idx].name
                if new_email == '':
                    new_email = self.clients[idx].email
                if new_address == '':
                    new_address = self.clients[idx].address
                if new_phone == '':
                    new_phone = self.clientss[idx].phone
                if new_rfc == '':
                    new_rfc = self.clients[idx].rfc
                new_client = Client(
                    self.clients[idx].id_client, new_name, new_email, new_address, new_phone, new_rfc)
                old_client = self.clients[idx]
                self.clients[idx] = new_client

            else:
                raise m_e.item_already_stored(
                    'Can\'t update "{}" because it\'s already stored'.format(new_name.upper())
                )
        else:
            raise m_e.item_not_stored('Cant\'t update "{}" because it\'s not stored'.format(old_name.upper()))
        return old_client, new_client

    def delete_a_client(self, name):
        idx = self.search_client(name)
        if idx > -1:
            del self.clients[idx]
        else:
            raise m_e.item_not_stored('Can\'t delete "{}" because it\'s not stored'.format(name.upper()))
