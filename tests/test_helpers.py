from ovpnWebman.helpers import check_password
import pytest

def test_check_password():
    """
    Password should be at least six characters with one number and one capital letter
    """
    assert check_password('Longpassword') == False
    assert check_password('123456') == False
    assert check_password('short') == False
    assert check_password('C0rect') == False
    assert check_password('Correct8') == True

