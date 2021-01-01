from caesar_cipher.caesar_ciper import *
from caesar_cipher import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual=encrypt('Great job Joudi',3)
    expected='juhdw mre mrxgl'
    assert actual==expected

def test_decrypt():
    actual=decrypt('Juhdw mre Mrxgl',3)
    expected='great job joudi'
    assert actual==expected  

def test_decrypt_with_caracters():
    actual=encrypt('Great job,@% Joudi',3)
    expected='juhdw mre,@% mrxgl'
    assert actual==expected  

def test_hack():
    actual=cipher_breaker('lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv.')
    expected='it was the best of times, it was the worst of times.'
    assert actual==expected      