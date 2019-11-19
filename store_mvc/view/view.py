class View:

    #productos

    def show_all_products(self, lista, b):
        if b:
            print('There are %i products in my DB. Here they are: ' % len(lista))
            print('-------------------Product list-------------------')
            for product in lista:
                details = str(product.id_product) + ' ' +product.name + ' ' + product.brand + ' '+\
                    product.category + ' ' +  \
                    str(product.price) + ' ' + \
                    str(product.weight) + ' ' + product.batch
                print('+ ' + details)
                print('_*_*_*_*_*_*_*_*_*_*_*_*_*' * 2)


    def show_a_product(self, product):
        print('********** Details for product')
        print('* ID:\t\t', product.id_product)
        print('* Name:\t\t', product.name)
        print('* Brand:\t', product.brand)
        print('* Category:\t', product.category)
        print('* Price:\t', product.price)
        print('* Weight:\t', product.weight)
        print('* Batch:\t', product.batch)
        print('***************************************************')

    def display_product_update(self, old_product, new_product):
        print('---------------------Product updated----------------------')
        print('* ID:\t\t', new_product.id_product)
        if old_product.name != new_product.name:
            print('* Name:\t\t', old_product.name, '-->', new_product.name)
        else:
            print('* Name:\t\t', new_product.name)
        if old_product.brand != new_product.brand:
            print('* Brand:\t', old_product.brand, '-->', new_product.brand)
        if old_product.category != new_product.category:
            print('* Category:\t', old_product.category, '-->', new_product.category)
        if old_product.price != new_product.price:
            print('* Price:\t', old_product.price, '-->', new_product.price)
        if old_product.weight != new_product.weight:
            print('* Price:\t', old_product.weight, '-->', new_product.weight)
        if old_product.batch != new_product.batch:
            print('* Price:\t', old_product.batch, '-->', new_product.batch)
        print('-------------------------------------------------------')

    def display_product_deleted(self, name):
        print('-------------------------------------------------------')
        print('You have selected {} from DB'.format(name.upper()))
        print('-------------------------------------------------------')

    #clientes hacerlos nosotros, son los mismos metodos que los productos

    def show_all_clients(self, lista, b):
        if b:
            print('There are %i clients in my DB. Here they are: ' % len(lista))
            print('-------------------Client list-------------------')
            for client in lista:
                details = str(client.id_client) + ' ' + client.name + ' ' + client.email + \
                    client.address + ' ' +  \
                    str(client.phone) + ' ' + \
                    client.rfc
                print('+ ' + details)
                print('_*_*_*_*_*_*_*_*_*_*_*_*_*' * 2)

    def show_a_client(self, client):
        print('********** Details for product')
        print('* ID:\t\t', client.id_client)
        print('* Name:\t\t', client.name)
        print('* Brand:\t', client.email)
        print('* Category:\t', client.address)
        print('* Price:\t', client.phone)
        print('* Weight:\t', client.rfc)
        print('***************************************************')


    def display_client_update(self, old_client, new_client):
        print('---------------------Client updated----------------------')
        print('* ID:\t\t', new_client.id_client)
        if old_client.name != new_client.name:
            print('* Name:\t\t', old_client.name, '-->', new_client.name)
        else:
            print('* Name:\t\t', new_client.name)
        if old_client.email != new_client.email:
            print('* Email:\t', old_client.email, '-->', new_client.client)
        if old_client.address != new_client.address:
            print('* Address:\t', old_client.address, '-->', new_client.address)
        if old_client.phone != new_client.phone:
            print('* Phone:\t', old_client.phone, '-->', new_client.phone)
        if old_client.rfc != new_client.rfc:
            print('* Rfc:\t', old_client.rfc, '-->', new_client.rfc)
        print('-------------------------------------------------------')


    def display_client_deleted(self, name):
        print('-------------------------------------------------------')
        print('You have selected {} from DB'.format(name.upper()))
        print('-------------------------------------------------------')


    #metodos de errores

    def item_not_stored_error(self, e):
        print('*********** ERROR ************')
        print('{}'.format(e.args[0]))
        print('************************')

    def item_already_stored_error(self, e):
        print('*********** ERROR ************')
        print('{}'.format(e.args[0]))
        print('************************')

    #General methosd

    def start_view(self):
        print('----- A second example of MVC ----------')

    def end_view(self):
        print('Goodbye!')

    def insert_a_product(self):
        print('Dame los datos del producto')
        print('Nombre')
        print('Marca')
        print('Categoria')
        print('Precio')
        print('Peso')
        print('Batch')

    def menu(self):
        print('Dame una opcion')
        print('1. Insertar un producto')
        print('2. Modificiar un producto')
        print('3. Mostrar un producto')
        print('4. Mostrar todos los productos')








