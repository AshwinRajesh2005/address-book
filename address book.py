s="address book menu"
b=s.title()
print(b)
contact={}
def address_book_menu():
    print ("1. add contact")
    print ("2. view contact")
    print  ("3. search contact")
    print ("4. delete contact")
    print ("5. EXIT")
address_book_menu()
your_choice=int(input("enter the choice from 1 to 5:"))
def add_contacts():
    contact_name=input("enter the contact_name:")
    contact_phone_number=int(input("enter the contact phone number:"))
    contact_email_address=input("enter the contact email address:")
    contact_address=input("enter the contact mailing address:")
    contact[contact_name]={"phone":contact_phone_number,"email":contact_email_address}
    print("contact add successfully")
    address_book_menu()
    your_choice=int(input("enter the choice from 1 to 5:"))
def view_contacts():
    if contact:
        print("contacts")
        for contact_name,details in contact.items():
            print(f"name:{contact_name},number:{details['contact_phone_phone']},email_address:{details['contact_email_address']}")
    else:
        print("no contact")
def search_contact():
    contact_name=input("enter the name to search:")
    if contace_name in contact:
        details=contact[contact_name]
        print(f"name:{contact_name},phone:{details['contact_phone_number']},email:{details['contact_email_address']}")
    else:
        print("contact not found")
if(your_choice==1):
    print(add_contacts())
elif(your_choice==2):
    print(view_contacts())
elif(your_choice==3):
    print(search_contact())

    



    
    
