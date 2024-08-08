
Contact = {}

def display_contact():
    print("name\t\t contact number")
    for key in Contact:
        print("{}\t\t{}".format(key,Contact.get(key))) 

while True:
    choice=int(input("1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Update contact \n 5. Exit:\n Enter your choice:"))
    if choice==1:
        name=input("Enter the contact name:")
        phone=input("Enter the mobile number :")
        Contact[name]=phone
    elif choice==2:
        search_name=input("Enter the contact name:")
        if search_name in Contact:
            print(search_name,"'s contact number is ",Contact[search_name])
        else:
            print("Name is not found in the contact book")
    elif choice==3:
        if not Contact:
            print("Contact is empty")
        else:
            display_contact() 
    elif choice==4:
        edit_contact=input("Enter the contact to be updated:")
        if edit_contact in Contact:
            phone = input("enter the mobile number:")
            Contact[edit_contact]=phone
            print("The contact is updated")
            display_contact()
        else:
            print("Name is not in the contact!!!!!")
    else:
        break