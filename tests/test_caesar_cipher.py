from caesar_cipher.caesar_ciper import *
from caesar_cipher import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual=encrypt('Great job Joudi',3)
    expected='Juhdw mre Mrxgl'
    assert actual==expected

def test_decrypt():
    actual=decrypt('Juhdw mre Mrxgl',3)
    expected='Great job Joudi'
    assert actual==expected  

def test_decrypt_with_caracters():
    actual=encrypt('Great job, Joudi',3)
    expected='Juhdw mre, Mrxgl'
    assert actual==expected  