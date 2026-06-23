import operation as op

while True:
    print("-"*30)
    print("      Welcome to do list!")
    print("-"*30)
    print("1. Add")
    print("2. Delete")
    print("3. View")
    print("4. Exit")
    
    user=input("Choose the option: ")
    # Conditional Flow
    try:
        if "1" in user:
            op.add()

        elif "2" in user:
            op.dlt()

        elif "3" in user:
            op.view()

        elif "4" in user:
            op.good_bye()
            break
        else:
            print("No Option")

    except Exception as e:
        print(f"Error: {e}")