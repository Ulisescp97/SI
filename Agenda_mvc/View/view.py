class View:
    """A simple view"""
    def show_all_contacts(self, contacts):
        print('********** In my db I have %i contacts. Here they are *********' % len(contacts))
        for contact in contacts:
            print(contact.first_name+'\t'+contact.last_name+'\t'+contact.email+'\t'+contact.tel)
        print('***************************************************************')

    def show_a_contact(self, contact):
        print('********** DETAILS FOR **********')
        print('* First name: '+contact.first_name)
        print('* Lastt name: '+contact.last_name)
        print('* Email: '+contact.email)
        print('* Telephone: '+contact.tel)
        print('*********************************')

    def start_view(self):
        print('MVC - A very simple example')

    def end_view(self):
        print('Thats it. GoodBye!')

    def contact_not_stored(self,e):
        print('****ERROR****')
        print(e.args[0])
        print('*************')    

    def contact_not_stored_error(self,e):
        print('****ERROR****')
        print(e.args[0])
        print('*************')

    def contact_already_stored_error(self,e):
        print('****ERROR****')
        print(e.args[0])
        print('*************')

    def create_a_contact(self):
        print('Dame los siguientes datos')
        print('* Nombre')
        print('* Apellido')
        print('* Correo')
        print('* Telefono')    

    def menu(self):
        print('MENU')
        print('1. Crear Contacto')
        print('2. Borrar Contacto')
        print('3. Actualizar')  
        print('4. Mostrar un contacto')
        print('5. Mostrar todos los contactos')
        print('6. Salir')                
        print('Dame una opcion') 