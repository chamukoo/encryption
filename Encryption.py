# Programmed by: Lee Anne Y. Angeles

while True:
    # Input Statement
    string = input("\nEnter a string to encrypt: ")

    # Replace() method to change the character 'a' to '*'
    char_a = string.replace('a', '*')
    # Replace() method to change the character 'e' to '&'
    char_e = char_a.replace('e', '&')
    # Replace() method to change the character 'i' to '#'
    char_i = char_e.replace('i', '#')
    # Replace() method to change the character 'o' to '+'
    char_o = char_i.replace('o', '+')
    # Replace() method to change the character 'u' to '!'
    char_u = char_o.replace('u', '!')

    # Output statement
    print("Encrypted string:", char_u.capitalize())

    try_again = input("\nWould you like to try again? [ y / n ] : ").lower()
    if try_again == 'y':
        continue
    else:
        print("\nThank you for using this program!\nGoodbye!")
        break


