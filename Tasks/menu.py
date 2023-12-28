print("Welcome to my shop! \n")
while True:
    menu = input("Select an option: \n \
             1. Add item \n \
             2. Remove item \n \
             3. Update item \n \
             4. Exit cart \
             : \t")
    #\t for tab and \ for next line     
    if menu == "1":
        print("Added item")
    elif menu == "2":
        print("Item removed")
    elif menu == "3":
        print("Item updated")  
    elif menu == "4":
        print("Good bye")  
        break        
    else:
        print("Invalid option")    