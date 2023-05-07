def encrypt(text):
    result = ""
    for i in range (0, len(text)):
        result = result + chr(ord(text[i]) + 4)
    return result

def decrypt(text):
    result = ""
    for i in range (0, len(text)):
        result = result + chr(ord(text[i]) - 4)
    return result

emote_winkingface = "\U0001F609"
emote_cryingface = "\U0001F622"


while True:
    print()
    choice = input("Choose what you want\n1 - Encrypt\n2 - Decrypt\n")
    print()

    if (choice =="1"):
        text = input("Enter the text you want to Encrypt: \n")
        encrypted_text = encrypt(text)
        print()
        print("Encrypted text: ", encrypted_text)
        print()

        restart_choice = input("Do you want to continue? (Y/N): ")
        if restart_choice.upper() == "N" or restart_choice.upper() == "NO":
            print()
            print("Exiting the program...", emote_cryingface)
            print()
            break

        elif restart_choice.upper() =="Y" or restart_choice.upper() == "YES":
            print()
            print("Welcome back!", emote_winkingface)

        elif restart_choice.upper() != "Y" or restart_choice.upper() != "YES":
            print()
            print("Invalid command, returning to menu...")
            print()
            print("Welcome back!", emote_winkingface)
                 
        


    elif (choice =="2"):
        text = input("Enter the text you want to Decrypt: \n")
        decrypted_text = decrypt(text)
        print()
        print("Encrypted text: ", decrypted_text)
        print()

        restart_choice = input("Do you want to continue? (Y/N): ")
        if restart_choice.upper() == "N" or restart_choice.upper() == "NO":
            print()
            print("Exiting the program...", emote_cryingface)
            print()
            break

        elif restart_choice.upper() =="Y" or restart_choice.upper() == "YES":
            print()
            print("Welcome back!", emote_winkingface)

        elif restart_choice.upper() != "Y" or restart_choice.upper() != "YES":
            print()
            print("Invalid command, returning to menu...")
            print()
            print("Welcome back!", emote_winkingface)
                 

    elif choice == "3":
        print ("Exiting the program...")
        break

    

    else:
        print()
        print("Invalid command, try again")
        print()

