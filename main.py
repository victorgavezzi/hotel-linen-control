items = []

while True:
    print("\n=== HOTEL LINEN CONTROL ===")
    print("1 - Register item")
    print("2 - List items")
    print("3 - Exit")

    option = input("Choose: ")

    if option == "1":
        code = input("Item code: ")
        item_type = input("Item type: ")

        items.append({
            "code": code,
            "type": item_type,
            "status": "Available"
        })

        print("Item registered successfully!")

    elif option == "2":
        if not items:
            print("No items registered.")
        else:
            for item in items:
                print(item)

    elif option == "3":
        print("Closing system...")
        break

    else:
        print("Invalid option.")
