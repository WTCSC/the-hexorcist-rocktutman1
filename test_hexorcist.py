import pytest, random
from hexorcist import to_decimal, from_decimal

def test_base10_to_decimal():
    assert to_decimal(10, '255') == 255
    assert to_decimal(10, '0') == 0
    assert to_decimal(10, '67') == 67

def test_base16_to_decimal():
    assert to_decimal(16, 'ff') == 255
    assert to_decimal(16, '0') == 0
    assert to_decimal(16, '1a3') == 419

def test_base2_to_decimal():
    assert to_decimal(2, '1010') == 10
    assert to_decimal(2, '0') == 0
    assert to_decimal(2, '11111111') == 255

def test_other_to_to_decimal():
    assert to_decimal(8, '17') == 15
    assert to_decimal(36, 'z') == 35
    assert to_decimal(5, '243') == 73

def test_decimal_to_base10():
    assert from_decimal(10, 255) == '255'
    assert from_decimal(10, 0) == ''
    assert from_decimal(10, 67) == '67'

def test_decimal_to_base16():
    assert from_decimal(16, 255) == 'ff'
    assert from_decimal(16, 0) == ''
    assert from_decimal(16, 419) == '1a3'

def test_decimal_to_other():
    assert from_decimal(8, 15) == '17'
    assert from_decimal(36, 35) == 'z'
    assert from_decimal(5, 73) == '243'

def test_random_to_decimal():
    alldigits = "0123456789abcdefghijklmnopqrstuvwxyz"
    base = random.randint(2, 36)
    digits = alldigits[:base]
    num_str = ""
    for i in range(random.randint(1, 7)):
        num_str += random.choice(digits )
    decimal_value = int(num_str, base)
    assert to_decimal(base, num_str) == decimal_value