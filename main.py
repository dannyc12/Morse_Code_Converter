from morse import morse_to_alpha, alpha_to_morse

# go from alpha to morse
def to_morse():
    string = input('Enter a string to convert to morse code: ')
    string.lower()
    listed_string = list(string)
    morse_list = [alpha_to_morse[char] for char in listed_string]
    joined_morse = ' '.join(morse_list)
    return joined_morse


def to_alpha():
    string = input('Enter morse code: ')
    listed_string = string.split('   ')
    # print(listed_string)
    alpha_conversion = []
    for item in listed_string:
        alpha_list = [morse_to_alpha[morse] for morse in item.split()]
        joined_alpha = ''.join(alpha_list)
        alpha_conversion.append(joined_alpha)
    return ' '.join(alpha_conversion)


continue_prompt = True


# ask user what to convert
def prompt():
    global continue_prompt
    response = input("What would you like to convert?\nFor Alpha-Numeric to Morse, enter: 1\n"
                     "For Morse to Alpha-Numeric, enter: 2\nTo quit, type: quit\n")
    if response == '1':
        print(f'Morse code conversion: {to_morse()}')
    elif response == '2':
        print('Enter your morse code with the following constraints: "."=dot, "-"=dash. Place one space " " between'
              'each morse code letter. Place three spaces "   " between words. '
              'For example: "high there" is ".... ..   - .... . .-. ."')
        print(f'Alpha-numeric conversion: {to_alpha()}')
    elif response == 'quit':
        continue_prompt = False
    else:
        print('Error: Please enter a valid choice')


while continue_prompt:
    prompt()
