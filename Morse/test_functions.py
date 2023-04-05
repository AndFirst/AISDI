import pytest
from functions import (get_morse_letter,
                       encode_line,
                       SmallLetterError,
                       SpaceError,
                       NotALetterError)


def test_code_big_letters():
    assert get_morse_letter('A') == '.-'
    assert get_morse_letter('O') == '---'
    assert get_morse_letter('S') == '...'

def test_code_small_letters():
    with pytest.raises(SmallLetterError):
        get_morse_letter('a')

def test_code_spaces():
    with pytest.raises(SpaceError):
        get_morse_letter(' ')

def test_code_other_characters():
    with pytest.raises(NotALetterError):
        get_morse_letter('6')

def test_encode_word_big_letters():
    assert encode_line('SOS') == '... --- ...'

def test_encode_word_small_letters():
    assert encode_line('sos') == '... --- ...'

def test_encode_word_mixed_letters():
    assert encode_line('sOs') == '... --- ...'

def test_encode_word_with_numbers():
    assert encode_line('5O5') == '---'

def test_encode_word_with_number_in_middle():
    assert encode_line('s3o') == '... ---'

def test_encode_text():
    assert encode_line('Ala ma kota') == '.- .-.. .- / -- .- / -.- --- - .-'

def test_encode_text_with_numbers():
    assert encode_line('a12b 3 c') == '.- -... / -.-.'

def test_encode_text_multiple_spaces():
    assert encode_line('sos     SOS') == '... --- ... / ... --- ...'

def test_encode_word_end_with_number():
    assert encode_line('so5 5os') == '... --- / --- ...'