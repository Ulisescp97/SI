from Model.contact import Contact
from Model.model import Model
from View.view import View

print('Hello world!')

c = Contact('German', 'Neftali', 'gnrg_74@hotmail.com', '4721005730')
print(c.email)

m = Model()
m.create_a_contact('Nefta', 'gonzalez', 'l@gmail.com', '1245')
m.create_a_contact('Javier', 'escuela', 'javi@ugto.mx', '145')
#m.create_a_contact('Oscar', 'Dominguez', 'oo.dominguez@ugto.mx', '12345')
print(m.read_all_contacts())
#print(m.read_a_contact('Javier', 'Lopez'))

m.update_a_contact('Javier', 'escuela', 'Nefta', 'gonzalez', 'gnrg_74@hotmai.com', '1545')
all_c = m.read_all_contacts()
contact = m.read_a_contact('Nefta', 'gonzalez')
print(m.read_all_contacts())
v = View()
v.show_a_contact(contact)

v.show_all_contacts(all_c)