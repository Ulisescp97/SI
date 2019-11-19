from Model.model import Model
from View.view import View
from Model import m_exceptions as m_e

class Controller:
    def create_a_contact(self,first_name,last_name,email = '',tel = ''):
        try:
            self.model.create_a_contact(first_name,last_name,email,tel)
        except m_e.contact_already_stored as e:
            self.view.contact_already_stored_error(e)

    def show_all_contacts(self):
        contacts = self.model.read_all_contacts()
        self.view.show_all_contacts(contacts)

    def show_a_contact(self,first_name,last_name):
        try:
            contact = self.model.read_a_contact(first_name,last_name)
            self.view.show_a_contact(contact)
        except m_e.contact_not_stored as e:
            self.view.contact_not_stored(e)

    def update_a_contact(self,old_first_name,olf_last_name,new_first_name,new_last_name,
                         new_email = '', new_tel = ''):
        try:
            self.model.update_a_contact(old_first_name,olf_last_name,new_first_name,new_last_name, new_email,new_tel)
        except m_e.contact_not_stored as e:
            self.view.contact_already_stored_error(e)

    def delete_a_contact(self,first_name,last_name):
        try:
            self.model.delete_a_contact(first_name,last_name)
        except m_e.contact_already_stored as e:
            self.view.contact_already_stored_error(e)   

    def start(self):
        self.model = Model()
        self.view = View()
        self.view.start_view() 
        self.create_a_contact('pedro','orozco','po@gmail.com')
        self.create_a_contact('luis','medrano')
        self.create_a_contact('luis','medrano')
        #self.delete_a_contact('juan','lopez')
        self.show_all_contacts()
        self.update_a_contact('juan','perez','luis','zapata','lz@gmail.com','4424232312')
        self.show_all_contacts()
        self.show_a_contact('luis','zapata')
        self.view.end_view()
    
    def menu(self):
        self.view = View()
        self.view.menu()
        a = input()
        if a == '1':
            self.view = View()
            self.view.create_a_contact()
            nombre = input()
            apellido = input()
            correo = input()
            telefono = input()
            self.create_a_contact(nombre,apellido,correo,telefono)
             





                                                                                        