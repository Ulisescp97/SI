from .contact import Contact
from . import m_exceptions as m_e #modulo para manejar excepciones

class Model:
    """A simple data model"""
    def __init__(self):
        self.contacts = []

    def search_contact(self, first_name, last_name):
        whole_name = first_name+' '+last_name
        for idx, contact in enumerate(self.contacts):
            if contact.first_name.lower()+' '+contact.last_name.lower() == whole_name.lower():
                return whole_name, idx
        return whole_name, -1


    def create_a_contact(self, first_name, last_name, email = '', tel = ''):
        whole_name, idx = self.search_contact(first_name, last_name)
        if idx < 0:
            self.contacts.append(Contact(first_name, last_name, email, tel))
        else:
            raise m_e.contact_already_stored('"{}" already stored'.format(whole_name.upper()))
    
    def read_all_contacts(self):
        return self.contacts

    def read_a_contact(self, first_name, last_name):
        whole_name, idx = self.search_contact(first_name, last_name)
        if idx > -1:
            return self.contacts[idx]
        else:
            raise m_e.contact_not_stored('Can\'t read contact "{}" because it\'s not stored'.format(whole_name.upper()))

    def update_a_contact(self, old_first_name, old_last_name,
                         new_first_name, new_last_name,
                         new_email, new_tel):
        whole_name, idx = self.search_contact(old_first_name, old_last_name)
        if idx > -1:
            new_contact = Contact(new_first_name, new_last_name, new_email, new_tel)
            whole_name_2, idx2 = self.search_contact(new_first_name, new_last_name)
            if idx2 > -1:
                raise m_e.contact_already_stored('Can\'t update "{}" because "{}" is already in database'.format(whole_name.upper(), whole_name_2.upper()))
            else:
                self.contacts[idx] = new_contact
        else:
            raise m_e.contact_not_stored('Can\'t update "{}" because it\'s not stored'.format(whole_name.upper()))
    
    def delete_a_contact(self, first_name, last_name):
        whole_name, idx = self.search_contact(first_name, last_name)
        if idx > -1:
            del self.contacts[idx]
        else:
            raise m_e.contact_not_stored('Can\'t delete "{}" because it\'s not stored'.format(whole_name.upper()))

        
