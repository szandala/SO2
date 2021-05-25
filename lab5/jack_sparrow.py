# print("Powitanie")

# str, int, float, boolean
# list, tuple, set, dict

# lista = [] # list()

# lista = ["abc", 1, 2, 3, 5.5, 2, False, 5.5]

# print(lista)
# # lista.append(555)
# # print(lista)

# # tupla = (1, 2, "text")

# ss = set()

# set_z_listy = set(lista)
# # print(set_z_listy)

# slownik = {
#     1: 'liczba'
#     'dwa': 2
#     5.5: True
# }


# def nazwa(param, param2="domyślna wartość"): # *param i **params
#     print("ciao funkcji")

#############################################################################
HANGMAN_PICS = [ "",
"""
+---+
    |
    |
    |
======
""",
"""
+---+
O   |
    |
    |
======
""",
"""
+---+
O   |
|   |
    |
======
""",
"""
 +---+
 O   |
/|   |
     |
======
""",
"""
 +---+
 O   |
/|\  |
     |
======
""",
"""
 +---+
 O   |
/|\  |
/    |
======
""",
"""
 +---+
 O   |
/|\  |
/ \  |
======
"""]




def check_letter_presence(new_letter, secret, found_letters):
    # ciekawostka: czy muszę zwracać found_letters? mutable/immutable
    is_letter_found = False

    for l in secret:
        if new_letter == l:
            print(f"{new_letter} found")
            found_letters.add(new_letter)
            is_letter_found = True
            break

    return found_letters, is_letter_found

def prepare_printing(secret, found_letters):
    printable_secret = ""

    for l in secret:
        if l == " ":
            printable_secret += " "
        elif l in found_letters:
            printable_secret += l
        else:
            printable_secret += "_ "

    return printable_secret

if __name__ == "__main__":
    secret = "Słup ognia"
    found_letters = set()
    failures_count = 0

    while True:
        letter = input("Podaj literę: ")
        print(f"Podales: {letter}")

        found_letters, is_failure = check_letter_presence(letter, secret, found_letters)

        if not is_failure:
            failures_count += 1
        # a, b, c = b, c, a
        # print(output)
        # found_letters, is_failure = output
        # print(is_failure)
        printable_secret = prepare_printing(secret, found_letters)

        # if failures_count == len(HANGMAN_PICS):
        #     print("Wtopiłeś, przegrałeś n00bie")
        #     break
        try:
            print(HANGMAN_PICS[failures_count])
        except IndexError:
            print("Wtopiłeś, przegrałeś n00bie")
            break

        # print(failures_count)
        print(printable_secret)
