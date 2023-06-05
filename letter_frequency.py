from collections import Counter


MESSAGE = "Wklv lv d sureohp wr nhhs wkh plqg ri pb pdwkhpdwlfv vwxghqwv hqjdjhg dqg wr pdnh wkhp xqghuvwdqg wkdw pdwkhpdwlfv lv d glvflsolqh ri wkh prvw lpsruwdqw ydoxh lq wkh zruog. Pdwkhpdwlfv lv qrw d glvflsolqh wkdw olyhv rqob lq whawerrnv. Hqfubswlqj phwkrgv kdyh ehhq xvhg vlqfh dqflhqw wlphv dqg wkh frpsohalwb ri wkhvh phwkrgv kdv lqfuhdvhg lpphqvhob vlqfh wkhq. Wkhvh phwkrgv duh lpsruwdqw lq ilqdqfh, zduiduh dqg srolwlfdo grpdlqv. Qrz brx nqrz krz rqh ri wkh roghvw dqg prvw vlpsoh fbskhuv zrun. L krsh L glg qrw jlyh brx d khdgdfkh."


def most_used_n(text : str, n : int = 3) -> tuple[str, int]:
    """
    Return a tuple of the most used letters in a text excluding " ", "," and "."
    """
    return Counter(
        text.lower().replace(" ", "").replace(".", "").replace(",", "")
    ).most_common(n)


def obtain_displacement(char : str) -> int:
    """
    Obtains n, where n is how many places to the right a letter
    is shifted in caesar cypher
    """
    # Most common char in english is "e"

    # Assume the letter >= "e"

    displacement = ord(char) - ord("e")

    if displacement < 0:
        raise Exception("This function doesn't contemplate the escenario where \"e\" < char D:")
    
    return displacement


def decode_caesars(text : str) -> None:
    """
    Decodes caesars cypher and prints message in screen
    """
    for k, _ in most_used_n(text, 1):
        displacement = obtain_displacement(k)
        
        for char in text.lower():
            # To maintain format
            if char in [".", " ", ","]:
                print(char, end="")
                continue
            # else
            # As caesars cypher shift to the right, we shift to the left by substracting
            ordi = ord(char) - displacement

            # If when we subtract we get something below "a"
            if ordi < ord("a"):
                # This is kind of hard to understand by plain text, draw it in a line and it's easy
                ordi = ordi + (ord("z") - ord("a")) + 1

            print(chr(ordi), end="")

        print("\n")


if __name__ == '__main__':
    decode_caesars(MESSAGE)

# EXTRA:

# Before using collections.Counter() I had made my own char counter :(

# def most_used_n(text : str, n : int = 3) -> Dict[str, int]:
#     freq_dict = {} # stores as {char  : count}
#     text = text.lower() # Lower case

#     # Iterate from a to z
#     for i in range(ord('a'), ord('z') + 1):
        
#         char_count = 0
#         for char in text:
#             if char == chr(i):
#                 char_count += 1
#         # Add the count of ocurrences of each char
#         freq_dict[chr(i)] = char_count
    
#     yield_dict = {}
#     inverse_freq_dict = [(value, key) for key, value in freq_dict.items()]
    
#     for _ in range(n):
#         # Add the maximum to the new dict
#         current_max = max(inverse_freq_dict)
#         yield_dict[current_max[1]] = current_max[0]

#         # Remove the maximum from the previous one
#         inverse_freq_dict.remove(current_max)
    
#     return yield_dict