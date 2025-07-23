while True:
    name = input("Enter your name (type 'exit' to stop): ")
    if name.lower() == 'exit':
        print("Goodbye!")
        break
    print("Hello,", name)
