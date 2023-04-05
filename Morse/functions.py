from alphabet import alphabet

class SmallLetterError(Exception):
    def __init__(self):
        super().__init__('Cannot replace small letter with morse code.')

class SpaceError(Exception):
    def __init__(self):
        super().__init__('Space cannot be replaced with morse code.')

class NotALetterError(Exception):
    def __init__(self):
        super().__init__('No letter character cannot be replaced with morse code.')

def get_morse_letter(letter:str)->str:
    if letter == ' ':
        raise SpaceError
    elif not letter.isalpha():
        raise NotALetterError
    elif letter.islower():
        raise SmallLetterError
    return alphabet[letter]

def create_code_letter(letter:str)->str:
    try:
        code_letter = get_morse_letter(letter) + ' '
    except SmallLetterError:
        code_letter = get_morse_letter(letter.capitalize()) + ' '
    except SpaceError:
        code_letter = '/ '
    except NotALetterError:
        code_letter = ''
    return code_letter

def add_letter(letter:str, ciphertext:str)->str:
    ciphertext += letter
    return ciphertext

def encode_line(line:str)->str:
    morse_line = ''
    line = leave_letters(line)
    line = unify_spaces(line)
    for character in line:
        letter = create_code_letter(character)
        morse_line = add_letter(letter, morse_line)
    return morse_line.rstrip()

def read_from_file(path:str)->str:
    with open(path) as handle:
        text = handle.readlines()
    return text

def encode_text(lines: list) -> str:
    text = ''
    for line in lines:
        line = encode_line(line)
        text += (line + '\n')
    return text.rstrip()

def leave_letters(line: str)->str:
    new_line = ''
    for char in line:
        if char == ' ' or char.isalpha():
            new_line += char
    return new_line

def unify_spaces(text:str) -> str:
    return ' '.join(text.split())

def encode_file(path:str) -> str:
    lines = read_from_file(path)
    text = encode_text(lines)
    return text
