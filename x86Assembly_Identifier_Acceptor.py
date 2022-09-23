# A Program to Check Whether a Name Can be Used as an Identifier in x86 Assembly or Not

error_code = 0
"""
Error Code's Guide:
0 -> Everything is Fine & the Entered Name Can be Used as an Identifier in Assembly
1 -> is Already a Reserved Keyword
2 -> Invalid Characters
3 -> Invalid Length
"""


# A Function to Check if Name is one of the Reserved Keywords of x86 Assembly Language or Not
def isReserved(Name):
    # Opening the File Which Contains All of the Reserved Keywords in Assembly Language
    file = open('Reserved_Keywords.txt', 'r')
    # Store Each Line (= 1 Keyword) from The Opened File into a List
    # Keywords Must Convert to LowerCase Before Storing (Because Assembly is not Case Sensitive) and also the Possible "\n" in the End of The Strings Most Be Omitted
    reserved_keywords = [
        keyword.lower()[:-1] if keyword.endswith("\n") else keyword.lower()
        for keyword in file.readlines()
    ]
    file.close()  # Closing the Opened File

    if Name in reserved_keywords:
        global error_code
        error_code = 1
        print(
            f"\nEntered Name is Already a Reserved Keyword of Assembly Language! (Error Code: {error_code})"
        )
        return True
    else:
        return False


# A Function to Check if Name's Characters are Valid or Not
def hasValidChars(Name):
    global error_code
    # First Character of the Name Only Can Be An Alphabetical Character ('A' to 'Z' or 'a' to 'z') or '_', '@', '?', '$'
    flag_first_character = False
    # Rest of the Characters of the Name Can be Alphabetical Character ('A' to 'Z' or 'a' to 'z') & '_', '@', '?', '$' & Also Digits
    flag_rest_characters = True

    first_character = Name[0]
    other_valid_characters = ['_', '@', '?', '$']

    # If the first Character is Alphabetical Character or '_', '@', '?', '$'; the Defined Flag (flag_first_character) Will Change to True
    if first_character.isalpha() or first_character in other_valid_characters:
        flag_first_character = True
    else:
        error_code = 2
        print(
            f"\nFirst Character of the Entered Name Isn't Valid! (Error Code: {error_code})"
        )

    # If The Rest of Characters are not Digits & not Alphabetical & not '_', '@', '?', '$'; the Defined Flag (flag_rest_characters) Will Change to False
    for character_index in range(1, len(Name)):
        if not (Name[character_index].isdigit()
                or Name[character_index].isalpha()
                or Name[character_index] in other_valid_characters):
            error_code = 2
            print(
                f"\n{character_index + 1}th Character of the Entered Name Isn't Valid! (Error Code: {error_code})"
            )
            flag_rest_characters = False

    return flag_first_character and flag_rest_characters


# A Function to Check if Name Has Acceptable Length or Not
def hasValidLen(Name):
    # Length of Name Shouldn't Be Greater than 247 and It Can't be None (NULL in Python)
    minimum_possible_length = 1
    maximum_possible_length = 247

    if minimum_possible_length <= len(Name) <= maximum_possible_length:
        return True
    else:
        global error_code
        error_code = 3
        print(
            f"\nEntered Name Doesn't Have Acceptable Length! (Error Code: {error_code})"
        )
        return False


# Getting a Name from User and Make it LowerCase
name = input("Please Enter the Name You'd Like to Check: ")
name = name.lower()

# Check if All of the Conditions Are Valid or Not
if hasValidLen(name) and hasValidChars(name) and not isReserved(name):
    print("Entered Name is Valid & Can be Used as an Identifier in Assembly.")
else:
    print("Entered Name CANNOT be Used as an Identifier in Assembly.")
