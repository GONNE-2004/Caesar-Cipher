import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    """holds the logic behind the encrypting and decrypting"""
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1 #force the shift backwards

    for letter in original_text:
        if letter.lower() not in alphabet: # by using lower function it forces any uppercase letter into
            output_text += letter # lowercase in order to check for it in the alphabet list but it keeps
        else:                      #any number&symbols untouched and only adds it letter to the output
            is_upper = letter.isupper() #checks whether there's any uppercase in the input and it'll be helpful later in changing it back
            shifted_position = alphabet.index(letter.lower()) + shift_amount #it first forces the letter to lowercase in order to get and shifts it's index in the alphabet list
            shifted_position %= len(alphabet) #ensure the shifts always within the list's bounds
            new_letter = alphabet[shifted_position] # it store the shfited inputs which are now lowercase
            output_text += new_letter.upper() if is_upper else new_letter # it stores the original input but converts any in them whic was uppercase to uppercase or else leaves it as it was
    print(f"Here is the {encode_or_decode}d result: {output_text}")
            #upper() converts lowercase to uppercase letters
            #isupper() checks if the letter is uppercase only so it's like true or false(boolean)

def main():
    """holds the main logic"""
    should_continue = True
    while should_continue:
        while True:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'Q' to exit!\n").lower()
            if direction in ["encode", "decode"]:
                break
            print("Invalid choice. Please enter 'encode' or 'decode'.")
            # the while loop is very useful in the upper validation because
            #  it allows the user more chances to input something from the list instead of a situation
            # where it's not used then if the user chooses wrongly the program crashes

        text = input("Type your message:\n")

        while True:
            shift_input = input("Type the shift number:\n")
            try:
                shift = int(shift_input)
                break
            except ValueError:
                print("invalid input. Please enter a digit number")
    # i could've just used this: shift = int(input(please enter a digit number)) in the upper codes which is shorter
    # but what if the user enters five or 3.14 the program would've crashed due to invalid input but
    # the try except saves the situation which when added with while loop prompts the user to try until they get it right,
    # though both code handle negative and positive integers well due to modulo % used in the caesar function


        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart == "no":
            should_continue = False
            print("Goodbye")
        elif restart == "yes":
            print("\n" * 20)





main()


