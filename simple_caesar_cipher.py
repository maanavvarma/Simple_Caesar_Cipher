# This is a simple caesar cipher implementation in Python.
# It shifts each letter by a specified number of positions in the alphabet.
# python 3 or higher is highly recommended before running this code
# python 3 helps sanitize input and handle exceptions better

# input for shift value
while True:
    # Get shift value with validation
    x = input("\nPlease enter the shift value (0-25) or \"G\" to exit: ").strip() # removes leading and trailing characters
    
    # Exit condition
    if x.lower() == "g":
        print("Exiting the program.")
        exit()
    
    # Validate input is digit
    while not x.isdigit():
        x = input("Invalid input. Please enter a number (0-25) or \"G\" to exit: ").strip()
        if x.lower() == "g":
            print("Exiting the program.")
            exit()
    
    shift = int(x)
    
    # Validate shift range
    while shift < 0 or shift > 25:
        print("Shift value must be between 0 and 25.")
        x = input("Please enter a valid shift value (0-25) or \"G\" to exit: ").strip()
        if x.lower() == "g":
            print("Exiting the program.")
            exit()
        while not x.isdigit():
            x = input("Invalid input. Please enter a number (0-25) or 'G' to exit: ").strip()
            if x.lower() == "g":
                print("Exiting the program.")
                exit()
        shift = int(x)
    
    # Get text to encrypt
    text = input("Please enter the text to be encrypted: ")
    
    # Encrypt text using Caesar cipher
    encrypted = ""
    for char in text:
        if char.isupper():
            # Shift uppercase characters
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            # Shift lowercase characters
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char
    
    # Output results
    print(f"Original text: {text}")
    print(f"Encrypted text: {encrypted}")
    print(f"Shift value used: {shift}\n")
